from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'billboard/index.html', {'posts': posts, 'form':form})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             # return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'billboard/post_edit.html', {'form': form})

#there should be defined something like post_detail function - it causes an error but it wasn't described in tutorial
def check_user(request):
    user = authenticate(username = 'john', password = 'secret')
    if user is not None:
        if user.is_active:
            print('User is valid')
        else:
            print('The password is valid, but the account was disabled!')
    else:
        print('information is incorrect')

def some_view(request):
    if request.user.is_authenticated():
        render(request, 'billboard/index.html', {'form': form})
    else:
        render(request, 'billboard/login.html', {'form' : form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            # redirect, or however you want to get to the main view
            return render(request, 'billboard/success.html')
    else:
        form = UserForm()
    return render(request, 'billboard/signup.html', {'form': form})

def success(request):
    return render(request, 'billboard/success.html')

@login_required
def post_new(request):
    form = form = PostForm()
    return render(request, 'billboard/post_edit.html', {'form': form})
