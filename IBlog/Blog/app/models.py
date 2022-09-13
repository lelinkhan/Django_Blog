from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style=width:60px;height:60px;border-radius:50% />'.format(self.image))

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def image_tag(self):
        return format_html('<img src="/media/{}" style=width:60px;height:60px;border-radius:50% />'.format(self.image))