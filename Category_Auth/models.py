from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(default="")
    slug = models.SlugField(max_length=300, default=name)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_id = models.AutoField
    category_id = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    img = models.ImageField(default="")

class Video(models.Model):
    video_id = models.AutoField
    category_id = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    videourl = models.URLField(max_length=250)

class User(AbstractUser):
    #email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.IntegerField(blank=True,null=True)
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    #USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


