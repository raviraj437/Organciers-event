from django.contrib import admin
from .models import Category
from .models import Image
from .models import Video
# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Video)