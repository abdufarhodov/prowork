from django.shortcuts import render
from django.urls import conf
from . models import Category,Blog,Hashtags,PicturesFromTheBlog,Regions
from django.utils.translation import gettext as _



###############################################################


def index(request):
    categories = Category.objects.all()
    blogs = Blog.objects.order_by('id')[::-1]
    hashtags = Hashtags.objects.all()
    rgn = Regions.objects.all()

    context = {
        'cat_objects':blogs,
        'categories':categories,
        'hash':hashtags,
        'rgn':rgn,
    }
    return render(request,'index.html',context)



################################################



def local(request):
    
    categories = Category.objects.all()
    blogs = Blog.objects.filter(is_local = True)
    hashtags = Hashtags.objects.all()
    rgn = Regions.objects.all()
    context = {

    'cat_objects':blogs,
    'categories':categories,
    'hash':hashtags,
    'rgn':rgn,
    }
    return render(request,'index.html',context)



####################################################


def cat_filter(request,slug):
    hashtags = Hashtags.objects.all()
    cats = Category.objects.all()
    a = Category.objects.get(slug = slug)
    s = a.blog_set.order_by('id')
    rgn = Regions.objects.all()
    context = {
        'cat_objects':s,
        'categories':cats,
        'hash':hashtags,
        'rgn':rgn,
    }
    return render(request,'index.html',context)


################################################################


def hash_filter(request,slug):
    cats = Category.objects.all()
    a = Hashtags.objects.get(slug = slug)
    s = a.hashtag.all()
    hashtags = Hashtags.objects.all()
    rgn = Regions.objects.all()
    context = {
        'cat_objects':s,
        'categories':cats,
        'hash':hashtags,
        'rgn':rgn,
    }
    return render(request,'index.html',context)


######################################################################


def detail(request,pk):
    hashtags = Hashtags.objects.all()
    cats = Category.objects.all()
    object = Blog.objects.get(id=pk)
    rgn = Regions.objects.all()
    context = {
        'object':object,
        'categories':cats,
        'hash':hashtags,
        'rgn':rgn,
    }
    return render(request,'detail.html',context)


#######################################################


def glob(request):
    
    categories = Category.objects.all()
    blogs = Blog.objects.filter(is_local = False)
    hashtags = Hashtags.objects.all()
    rgn = Regions.objects.all()
    context = {

    'cat_objects':blogs,
    'categories':categories,
    'hash':hashtags,
    'rgn':rgn,
    }
    return render(request,'index.html',context)


##############################################################################


def region(request,slug):
    blogs = Blog.objects.order_by('id')
    categories = Category.objects.all()
    hashtags = Hashtags.objects.all()
    regions = Regions.objects.all()
    b = Regions.objects.get(slug = slug)
    c = b.blog_set.order_by('id')
    context = {
        'cat_objects':c,
        'rgn':regions,
        'hash':hashtags,
        'categories':categories,
    }
    return render(request,'index.html',context)