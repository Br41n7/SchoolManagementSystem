from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request, category_slug=None):
    category = None
    posts = Post.objects.filter(published=True).order_by('-created_at')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
