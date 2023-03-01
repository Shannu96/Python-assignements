from django.db import models

# Create your models here.
class Login_User(models.Model):
    name = models.CharField(max_length=255)
    userId = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length = 255)

    #def__str__(self):
        #return f"{self.name} {self.userId}"

