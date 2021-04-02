from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.id}'

class Collection(models.Model):
    name = models.CharField(max_length=255)
    img = models.FileField()

    # {
    #     'id': 1,
    #     'name': 'collection name',
    #     'img': 'source',
    #     'products': [
    #         12, 13, 34
    #     ]
    # }

    def __str__(self):
        return f'{self.name} - {self.id}'
        
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name} - {self.code}'


class Catalog(models.Model):
    name = models.CharField(max_length=300)
    img = models.FileField()

    def __str__(self):
        return f'{self.name} - {self.id}'

class Image(models.Model):
    name = models.CharField(max_length=200)
    img = models.FileField()

    def __str__(self):
        return f'{self.name} - {self.id}'
        
class Product(models.Model):
    name = models.CharField(max_length=1000)
    seo_name = models.SlugField(max_length=1000)
    quantity = models.IntegerField()
    vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    collection = models.ManyToManyField(Collection, related_name='products')
    images = models.ManyToManyField(Image, related_name='products')

    def __str__(self):
        return f'{self.name} - {self.id}'



    # {
    #     'id': 1,
    #     'name': 'test name',
    #     'seo_name': 'test_name',
    #     'quantity': 43,
    #     'vendor': 1,
    #     'product_type': 2,
    #     'collections': [
    #         1, 2, 3
    #     ]
    # }