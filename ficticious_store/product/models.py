from django.db import models

# Create your models here.


class Product(models.Model):

	name = models.CharField('Name', max_length=100)	

	price = models.DecimalField('Price', decimal_places=2, max_digits=8)

	quantity = models.IntegerField('Quantity in Inventory')

	def __str__(self):

		return self.name
