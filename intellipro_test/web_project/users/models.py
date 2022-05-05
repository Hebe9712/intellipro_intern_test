"""
Models of web project

models:
    Label: a label model

"""
from django.db import models
from django.conf import settings
# Create your models here.


class Label(models.Model):
    """
    Label Model
    attributes:
        title: name of the label
        user: user that the label belongs to
    """
    title = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="label_item", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

