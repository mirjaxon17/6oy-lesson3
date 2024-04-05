from django.db import models
from student.models import Student




class Autor(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     birth_date = models.DateField(auto_now_add=True)
     def __str__(self):
          return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
     author = models.ForeignKey(Autor,null=True, on_delete=models.CASCADE)
     text = models.TextField()
     students = models.ForeignKey(Student, on_delete=models.CASCADE)

     def __str__(self):
          return f"{self.text} - {self.author}"
class Book(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField()
     coments = models.ManyToManyField(Comment)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     author = models.ForeignKey(Autor, on_delete=models.CASCADE)
     count = models.IntegerField(default=1)


     def __str__(self):
          return f"{self.name} - {self.price}"


class BookingBook(models.Model):
     students = models.ManyToManyField(Student)
     take_date = models.DateField(auto_now_add=True)
     book = models.ManyToManyField(Book)
     return_date = models.DateField(default=False)
     rent_price = models.FloatField(default=0)

     def __str__(self):
          return f"{self.students}{self.book}"