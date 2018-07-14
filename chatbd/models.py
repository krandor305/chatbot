from django.db import models

class Chat(models.Model):
    message=models.CharField(max_length=60)
    

