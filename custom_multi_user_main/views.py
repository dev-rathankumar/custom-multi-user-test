from django.shortcuts import render
from accounts.models import Auto
from django.http import HttpResponse

def home(request):
    customer_id = Auto.objects.filter().values_list('customer_id', flat=True)
    return HttpResponse(customer_id)
    exit()
    context = {
        customer_id : 'customer_id',
    }
    return render(request, 'accounts/index.html', context)
