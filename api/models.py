from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=1000)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'Product id={self.id}, ' \
               f'name= {self.name}, ' \
               f'description= {self.description}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category,
        }
