from django.db import models
from authentication.models import User

import os

def get_dynamic_path(instance, filename):
    username = instance.user.username
    upload_path = os.path.join('uploads', username)
    return upload_path


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_dynamic_path)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
