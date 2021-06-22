from django.db import models


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=128, default='Category', verbose_name='Category')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Name = models.CharField(max_length=256, default='Sub Category', verbose_name='Sub Category')

    def __str__(self):
        return f'{self.Name}/{self.Category.Name}'

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'


class Product(models.Model):
    ProductName = models.CharField(max_length=256, default='Name', verbose_name='Product Name')
    SKU = models.CharField(max_length=128, default='SKU', verbose_name='Product SKU')

    BotanicalName = models.CharField(max_length=256, default='Botanical Name', null=True, blank=True)
    PlantPartUsed = models.CharField(max_length=256, default='Plant Part', null=True, blank=True)

    ProcessingMethod = models.CharField(max_length=512, default='Processing Method', null=True, blank=True)
    ProductType = models.CharField(max_length=128, default='Product Type')

    Description = models.TextField(max_length=10000, default='Description', null=True, blank=True)
    ShelfLife = models.CharField(max_length=10, default='1', verbose_name='Self Life in Months', null=True, blank=True)

    SubCategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, default=1, null=True, blank=True)

    Potency = models.CharField(max_length=512, default=' ', null=True, blank=True)
    Source = models.CharField(max_length=512, default=' ', null=True, blank=True)
    ProductForm = models.CharField(max_length=512, default=' ', null=True, blank=True)
    Temperature = models.CharField(max_length=512, default=' ', null=True, blank=True)
    Method = models.CharField(max_length=512, default=' ', null=True, blank=True)

    Image = models.ImageField(upload_to='product_images/', null=True, blank=True, default='product_images/alt.png')

    def __str__(self):
        return f'{self.ProductName} {self.SKU}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Tag(models.Model):
    Name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(models.Model):
    Date = models.DateField(auto_now_add=True)
    Title = models.CharField(max_length=5000, default='Title')
    Image = models.ImageField(upload_to='blog_images', default='blog_images/default.png')
    Content = models.TextField()
    Tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.Date} {self.Tags}'

    def get_tags(self):
        return "\n".join([t.Name for t in self.Tags.all()])

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
