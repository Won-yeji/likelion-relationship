from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog, Comment, Tag, Like


def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog)
    tags = blog.tag.all()
    like_blog = Like.objects.filter(blog=blog)
    like_count = like_blog.count()
    
    context = {
        'blog': blog,
        'comments': comments,
        'tags': tags,
        'like_blog': like_blog.first() if like_blog.exists() else None,
        'like_count': like_count,
    }
    return render(request, 'detail.html', context)



def new(request):
    tags = Tag.objects.all()
    return render(request, 'new.html', {'tags': tags})


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('image')
    new_blog.author = request.user

    new_blog.save()
    tags = request.POST.getlist('tags')

    for tag_id in tags:
        tag = Tag.objects.get(id=tag_id)
        new_blog.tag.add(tag)

    return redirect('detail', new_blog.id)


def edit(request, blog_id):
    # edit_blog = get_object_or_404(Blog, pk=blog_id)
    edit_blog = Blog.objects.get(id=blog_id)

    if request.user != edit_blog.author:
        return redirect('home')

    return render(request, 'edit.html', {'edit_blog': edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')


def create_comment(request, blog_id):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.blog = get_object_or_404(Blog, pk=blog_id)
    comment.author = request.user
    comment.save()
    return redirect('detail', blog_id)


def new_comment(request, blog_id):
    if request.user.is_anonymous:
        return redirect('login')
    
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'new_comment.html', {'blog': blog})


# TODO: like 기능 구현
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.user.is_anonymous:
        return redirect('login')
    
    if request.user.is_authenticated:
        like = Like.objects.filter(blog=blog, user=request.user).first()
        if like:
            # 이미 좋아요를 누른 경우
            like.delete()
        else:
            # 좋아요를 누르지 않은 경우
            like = Like(user=request.user, blog=blog)
            like.save()

    return redirect('detail', blog_id)
