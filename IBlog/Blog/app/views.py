from django.db.models import Q
from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    all_post = Post.objects.all()[:]
    all_category = Category.objects.all()
    context = {'all_post':all_post,'all_category':all_category}
    return render(request, 'home.html', context)


def post(request,url):
    single_post = Post.objects.get(url=url)
    all_category = Category.objects.all()
    context = {'single_post':single_post,'all_category':all_category}
    return render(request,'posts.html',context)


def category(request,url):
    all_category = Category.objects.all()
    cats = Category.objects.get(url = url)
    posts = Post.objects.filter(cat=cats)
    context = {'cats':cats,'posts':posts,'all_category':all_category}
    return render(request,'category.html',context)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            posts = Post.objects.filter(Q(title__icontains = query) | Q(url__icontains = query) | Q(content__icontains = query))
            context = {'posts':posts}
            return render(request,'search.html',context)
        else:
            return render(request, 'search.html', {'message':'Sorry!! No Match!'})