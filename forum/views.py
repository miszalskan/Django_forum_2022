from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostAddForm, CommentForm
from django.http import HttpResponseRedirect

from .models import Post, Comment


def index(request):
    posts = Post.objects.all().order_by('-updated_on')
    context = {'post_list': posts}
    return render(request, 'indeks.html', context=context)


def about(request):
    return render(request, 'about.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def add_post(request):
    submitted = False
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = PostAddForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_post.html', {'form': form, 'submitted': submitted})


def add_comment(request, pk):
    post = Post.pk
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm
    return render(request, 'add_comment.html', {'form': form})

