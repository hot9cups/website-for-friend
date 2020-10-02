from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    mobile_extn = models.CharField(max_length=3)
    mobile_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.contact_id) + ' -> ' + self.name

