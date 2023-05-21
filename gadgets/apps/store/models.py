from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    data_added = models.DateTimeField(auto_now_add=True)

    # image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    # thumbnail = models.ImageField(blank=True, null=True, upload_to='uploads/')

    class Meta:
        ordering = ('-data_added',)

    def __str__(self) -> str:
        return self.title
    
    # def save(self, *args, **kwargs):
    #     self.thumbnail = self.MakeThumbnail(self.image)

    #     super().save(*args, **kwargs)
    
    # def MakeThumbnail(self, image, size=(300,200)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)

    #     thumb = File(thumb_io, name=image.name)

    #     return thumb


    