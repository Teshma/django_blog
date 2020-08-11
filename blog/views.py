from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, CV
from .forms import PostForm, CVForm
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})

##TODO
def view_cv(request):
    cv = CV.objects.first()
    print(cv)
    if cv:
        return render(request, "blog/cv.html", {"cv": cv})
    else:
        return render(request, "blog/cv.html", {"cv": False})

def new_cv(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            CV = form.save(commit=False)
            CV.author = request.user
            CV.save()
            return redirect("view_cv")
    else:
        form = CVForm()
    return render(request, "blog/cv_edit.html", {"form": form})

def edit_cv(request):
    return render(request, "blog/cv.html")

def delete_cv(request):
    CV.objects.first().delete()
    return redirect("view_cv")