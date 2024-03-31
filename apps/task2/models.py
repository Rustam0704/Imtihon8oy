from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    profession = models.CharField(max_length=128)
    age = models.IntegerField()
    city = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.title
