from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def home(request):
    form = SignupForm()
    return render(request, 'core/register.html', {'form':form})
