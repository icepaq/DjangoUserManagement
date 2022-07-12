from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    role = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name