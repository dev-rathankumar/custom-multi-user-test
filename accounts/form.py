from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Business, User
from django import forms

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    customer_location = forms.CharField(required=True)
    customer_pin_code = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic # If the block of code is successfully run, then the changes are saved in the database and if there's an exception then the changes will be rolled back.
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.customer_location = self.cleaned_data.get('customer_location')
        customer.customer_pin_code = self.cleaned_data.get('customer_pin_code')
        customer.save()
        return user

class BusinessSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    business_company_name = forms.CharField(required=True)
    business_city = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic # If the block of code is successfully run, then the changes are saved in the database and if there's an exception then the changes will be rolled back.
    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        business = Business.objects.create(user=user)
        business.business_company_name = self.cleaned_data.get('business_company_name')
        business.business_city = self.cleaned_data.get('business_city')
        business.save()
        return user
