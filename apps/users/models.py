from django.db import models

class Category(models.Model):

    category_title = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="Category")
    category_description = models.TextField()


    class Meta:
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.category_title

class Product(models.Model):

    product_title = models.CharField(max_length=255)
    product_image = models.ImageField()
    product_description = models.TextField()
    product_date_added = models.DateTimeField()
    product_category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'

    def __str__(self):
        return self.product_title

class Services(models.Model):
    services_title = models.CharField(max_length=255)
    services_description = models.TextField()
    services_image = models.ImageField()
    services_category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.services_title

class about_us(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to="about_us")

    class Meta:
        verbose_name = 'О нас'

    def __str__(self):
        return self.title

class News(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()
    img_poster = models.ImageField(upload_to='News')


