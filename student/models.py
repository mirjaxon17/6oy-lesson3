from django.db import models

# Create your models here.
class Adress(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Role(models.TextChoices):
    degree = ("degree", "B")
    master = ("master", "M")
    professor = ("professor", "P")


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=Role.choices ,default=Role.degree )
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    address = models.ForeignKey(Adress,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"