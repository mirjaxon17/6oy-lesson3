from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField(null=True)
    price = models.FloatField()
    count = models.IntegerField(default=1, null = True)
    create_date = models.DateTimeField(auto_created=True,null = True )
    class Meta:
        db_table ="book"

    def __str__(self):
        return f"{self.title} {self.price}"
