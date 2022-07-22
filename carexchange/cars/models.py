from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"


class Cars(models.Model):
    def __str__(self):
        return self.name

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    year_of_production = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


