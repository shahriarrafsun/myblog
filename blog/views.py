from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Poem, Blog, About
# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def poemlist(request):
    all_poems = Poem.objects.order_by("-published_date")
    paginator = Paginator(all_poems, 4)
    page_number = request.GET.get('page')
    try:
        poems = paginator.page(page_number)
    except PageNotAnInteger:
        poems = paginator.page(1)
    except EmptyPage:
        poems = paginator.page(paginator.num_pages)
    context = {'poems': poems}
    return render(request, 'blog/poemlist.html', context)


def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    context = {'poem': poem}
    return render(request, 'blog/poem_detail.html', context)


def bloglist(request):
    all_blogs = Blog.objects.order_by("-published_date")
    paginator = Paginator(all_blogs, 4)
    page_number = request.GET.get('page')
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {"blogs": blogs}
    return render(request, 'blog/bloglist.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)


def about(request):
    about_info = About.objects.first()
    context = {"about_info": about_info}
    return render(request, 'blog/about.html', context)
