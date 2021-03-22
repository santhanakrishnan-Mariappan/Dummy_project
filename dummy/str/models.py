from uuid import uuid4
from django.db import models


class model_class(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

