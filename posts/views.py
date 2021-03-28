# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.forms import PostForm


posts = []

@login_required()
def list_posts(request):
    profile = request.user.profile
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts, 'profile': profile})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={'form': form, 'user': request.user, 'profile': request.user.profile}
    )