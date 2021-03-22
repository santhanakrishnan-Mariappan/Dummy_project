from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import form_class
from .models import model_class
from django.core.mail import  EmailMessage


def regiter(request):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Record created successfully')
        return HttpResponse(f'Record not created')
    else:
        form = form_class()
        return render(request, 'file1.html', {'form': form})

def get_all_record(request):
    if request.method == 'GET':
        records = model_class.objects.all()
        return render(request, 'getall.html', {'records': records})

def get_filter_record(request):
    if request.method =='GET':
        records =  model_class.objects.filter(name='Zoro')
        return render(request, 'getall.html', {'records': records})

def get_particular_record(request):
    if request.method == 'GET':
        record = model_class.objects.get(name='Zoro')
        return render(request, 'get_particular.html',{'record': record})

def update_record(request,x):
    record = model_class.objects.get(name=x)
    if request.method == 'POST':
        form = form_class(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return render(request, 'get_particular.html', {'record': form})
    else:
        form = form_class(instance=record)
        return render(request, 'file1.html', {'form': form})

def delete_record(request,x):
    record = model_class.objects.get(name=x)
    if request.method == 'POST':
        record.delete()
        return HttpResponse(f'Record deleted')
    else:
        form = form_class(instance=record)
        return render(request, 'file1.html', {'form': form})


def send_mail(request):
    # POST REQUEST
    if request.method == 'POST':
        your_name = request.POST['name']
        phno = request.POST['mobile']
        contact_email = request.POST['mail']
        course = request.POST['course']


        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + contact_email + '\n' + str(
            phno) + '\n' + course
        email = EmailMessage(subject, content, to=[contact_email])
        email.send()
        return HttpResponseRedirect('/submit/')

    return render(request, 'stdform.html', {})

def submit(request):
    return HttpResponse('<h1> Record Submitted</h1>')






