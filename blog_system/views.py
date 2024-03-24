from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('blog_post_list_doctor')
    else:
        form = BlogPostForm()
    return render(request, 'blog_system/blog_post_create.html', {'form': form})

def blog_post_list(request):
    posts = BlogPost.objects.filter(draft=False)
    return render(request, 'blog_system/blog_post_list.html', {'posts': posts})


from django.shortcuts import render
from .models import BlogPost

def blog_post_list_doctor(request):
    # Get all blog posts uploaded by the current doctor user, including drafts
    posts = BlogPost.objects.filter(user=request.user)
    return render(request, 'blog_system/doctor_blog_post_list.html', {'posts': posts})


from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list_doctor')  
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_system/edit_post.html', {'form': form})

