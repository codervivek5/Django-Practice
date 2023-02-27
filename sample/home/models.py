from django.db import models

# Create your models here.
class Contact(models.Model):
    fName = models.CharField(max_length=122)
    lName = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Subject = models.CharField(max_length=122)
    Message = models.TextField(default='Write ur message')
    date = models.DateField()

    def __str__(self):
        return self.fName