from django.db import models


class Message(models.Model):
    author = models.CharField(verbose_name='Author', db_index=True, max_length=64)
    email = models.EmailField(verbose_name='Email', max_length=64)
    text = models.CharField(verbose_name='Text', max_length=100)
    create_date = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Update date', auto_now=True)
