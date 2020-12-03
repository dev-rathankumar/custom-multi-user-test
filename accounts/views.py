from django.shortcuts import render
from django.views.generic import CreateView
from .models import User, Business, Customer
from .form import CustomerSignUpForm, BusinessSignUpForm

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

class customerRegister(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customerRegister.html'


class businessRegister(CreateView):
    model = User
    form_class = BusinessSignUpForm
    template_name = 'accounts/businessRegister.html'
