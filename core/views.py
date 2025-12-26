from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/register.html', {'form':form})
