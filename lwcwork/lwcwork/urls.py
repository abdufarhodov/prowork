from django.conf.urls import url
from django.contrib import admin
from django.urls import conf, path,include
from django.conf import settings
from django.conf.urls.static import static
from lwcapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name= 'index'),
    path('cat-filter/<str:slug>',views.cat_filter,name= 'cat_filter'),
    path('local/',views.local,name= 'local'),
    path('hashtag/<str:slug>',views.hash_filter,name= 'hash_filter'),
    path('region/<str:slug>',views.region,name= 'region'),
    path('detail/<int:pk>',views.detail,name= 'detail'),
    path('glob/',views.glob,name= 'glob'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)