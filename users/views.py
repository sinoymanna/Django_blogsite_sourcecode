
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserRegisteraationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisteraationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}! ')

            return redirect('blog-homepage')
    else:
        form = UserRegisteraationForm()
    return render(request, 'users/register.html', {'form': form})
