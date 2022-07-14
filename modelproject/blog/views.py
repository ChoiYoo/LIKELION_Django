from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-time')

    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(title__contains=query)
    typecheck = request.GET.get('typecheck')
    if typecheck:
        blogs = Blog.objects.filter(type__contains=typecheck)
    paginator = Paginator(blogs, 4)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' : paginated_blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    form = CommentForm()
    return render(request, 'detail.html', {'blog' : blog, 'form':form})

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body  = request.POST['body']
        blog.save()
        return redirect('blog:detail', blog.id)
    return render(request, 'update.html', {'blog' : blog})

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')

def new_form(request):
    if request.user.is_authenticated:
        form = BlogForm()
        return render(request, 'new_form.html', {'form':form})
    return redirect('account:login')

def create_form(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.time = timezone.now()
        if request.user.is_authenticated:
            new_blog.user = request.user
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')

def create_comment(request, id):
    blog = get_object_or_404(Blog, pk=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.time = timezone.now()
        if request.user.is_authenticated:
            comment.user = request.user
        comment.post = blog
        comment.save()
    return redirect('blog:detail', blog.id)

def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    blog_id = comment.post.id
    comment.delete()
    return redirect('blog:detail', blog_id)