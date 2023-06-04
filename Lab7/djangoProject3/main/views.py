from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.
from .models import *
from .forms import OrderForm, CustomerForm, ProductForm, UserCreationForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'delete.html', context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'customer_form.html', context)


def deleteCustomer(request, pk):
    curr_customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        curr_customer.delete()
        return redirect('/')

    context = {'item': curr_customer}
    return render(request, 'delete_customer.html', context)


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'product_form.html', context)


def updateProduct(request, pk):
    curr_product = Product.objects.get(id=pk)
    form = ProductForm(instance=curr_product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=curr_product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'product_form.html', context)


def deleteProduct(request, pk):
    curr_product = Product.objects.get(id=pk)
    if request.method == "POST":
        curr_product.delete()
        return redirect('/')

    context = {'item': curr_product}
    return render(request, 'delete_product.html', context)


def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
