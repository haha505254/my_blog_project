from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
     context = {
         'form': UserCreationForm
     }
     return render(request, 'account/register.html', context)