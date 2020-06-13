from django.contrib import admin
from .models import Category
from .models import Image
from .models import Video
from .models import Event
from .models import Testmonial
from .models import ImageTestmonial
# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Event)
admin.site.register(Testmonial)
admin.site.register(ImageTestmonial)
