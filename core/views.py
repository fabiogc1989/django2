from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm, ProductModelForm
from .models import Product

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() == True:
            form.send_mail()
            messages.success(request = request, message = 'E-mail sent successfuly')
            form = ContactForm()
        else:
            messages.error(request = request, message = 'Something went wrong sending an e-mail')


    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfuly')
        else:
            messages.error(request, 'Error of saving product')
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, 'product.html', context)
