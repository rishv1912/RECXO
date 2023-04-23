from django.db import models

# Create your models here.


class Home(models.Model):
    email = models.EmailField(max_length=200)
    password = models.TextField(max_length=8)
    con_password = models.TextField(max_length=8)
    fullname = models.TextField(max_length=20)
    username = models.TextField(max_length=20)
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    message = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    soft_name = models.CharField(max_length=120)
    soft_type = models.CharField(max_length=120)
    soft_time = models.CharField(max_length=120)
    soft_amount = models.CharField(max_length=120)
    soft_desc = models.CharField(max_length=120)

    def __str__(self):
        return self.soft_name

class GetJob(models.Model):
    name = models.CharField(max_length=120)
    UserName = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    education = models.CharField(max_length=120)
    qualification = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    your_skills = models.CharField(max_length=120)
    ever_worked = models.CharField(max_length=120)
    jobrole = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    describe = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.UserName} {self.name} {self.jobrole}"
