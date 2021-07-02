from django.contrib import admin
from . models import Blog,Category,Hashtags,Regions,PicturesFromTheBlog

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Hashtags)
admin.site.register(Regions)
admin.site.register(PicturesFromTheBlog)