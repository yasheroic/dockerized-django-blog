from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "home.html", {"posts": posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect("home")
    return render(request, "create_post.html")