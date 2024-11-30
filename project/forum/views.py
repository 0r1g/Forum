from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Branch, Post, Comment
from .forms import PostForm, CommentForm


@login_required
def show_all_branches(request):
    branches = Branch.objects.all()
    posts = Post.objects.filter(views__gt=0).order_by('-views')
    return render(request, 'forum/list_branches.html', {'branches': branches, 'posts': posts})


@login_required
def show_all_posts(request, branch_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.branch = Branch.objects.get(id=branch_id)
            post.save()
            return redirect('post', post_id=post.id)
    else:
        form = PostForm()

    branch = Branch.objects.get(id=branch_id)
    posts = Post.objects.filter(branch=branch).order_by('-created_at')
    return render(request, 'forum/list_posts.html', {'posts': posts, 'form': form})


@login_required
def show_post(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('post', post_id=post_id)
    else:
        form = CommentForm()
    post = get_object_or_404(Post, id=post_id)

    viewed_posts = request.session.get('viewed_posts', [])

    if post_id not in viewed_posts:
        post.views += 1
        post.save()

        viewed_posts.append(post_id)
        request.session['viewed_posts'] = viewed_posts

    comments = Comment.objects.filter(post=post)
    return render(request, 'forum/show_post.html', {'post': post, 'comments': comments, 'form': form})
