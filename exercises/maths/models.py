from django.db import models

# Create your models here.
class Math(models.Model):
    operation = models.CharField(max_lenght=10)
    arg_a = models.IntegerFiled()
    arg_b = models.IntegerFiled()

    def