"""
Forms of web project

forms:
    LabelForm: form for create the label

"""
from django.forms import ModelForm
from .models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = "__all__"

