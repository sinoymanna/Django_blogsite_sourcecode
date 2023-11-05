
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisteraationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisteraationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!,You can now Login')

            return redirect('login')
    else:
        form = UserRegisteraationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render (request,'users/profile.html')


                   