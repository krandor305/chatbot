from . import models
from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='message', max_length=100)

