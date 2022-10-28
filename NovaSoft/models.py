from django.db import models

class Developer(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    name = models.CharField(max_length=20)
    work = models.CharField(max_length=12)
    image = models.ImageField(upload_to='Developer/%Y/%m')

    def __str__(self):
        return f'{self.name} - {self.work}'


class Contact(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=14)
    mail = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Get in touch'
        verbose_name_plural = 'Get in touch'

    def __str__(self):
        return f'{self.name} - {self.number}'

# Create your models here.
