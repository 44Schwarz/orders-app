from django.db import models

# Create your models here.


class Order(models.Model):
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.description
