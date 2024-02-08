from django.db import models

# Create your models here.
class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField (max_length=50)
    email = models.EmailField()
    phone = models.CharField (max_length=13)
    content = models.TextField()

    def __str__(self):
        return "message from "+ self.name


