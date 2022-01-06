from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils import timezone
from django.core.paginator import Paginator

from datetime import datetime, timedelta
from .models import Product, Category, SubCategory, Blog, View_Ips, AboutUs
from .forms import *


# Create your views here.

def home(request):
    if request.method == 'POST':
        var = request.POST.get('search')
        obj = get_object_or_404(Product, ProductName=var)
        return redirect('core:detail', obj.id)
    else:
        dot = datetime.now(tz=timezone.utc)
        d = timedelta(days=14)
        sub = dot - d

        category = Category.objects.all()
        popular_prods = Product.objects.all().order_by('views')[:8]
        trending_prods_id = View_Ips.objects.filter(Date__range=[sub, dot]).values('Product_id')
        trending_prods = Product.objects.filter(pk__in=trending_prods_id).order_by('views')[:8]
        prods = Product.objects.all()

        context = {
            'category': category,
            'popular_products': popular_prods,
            'trending_products': trending_prods,
            'prods': prods,
        }

        return render(request, 'core/landing.html', context)


def products(request):
    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    prod = Product.objects.all()

    prod_paginator = Paginator(prod, 20)

    page_num = request.GET.get('page')

    page = prod_paginator.get_page(page_num)

    context = {
        'category': cat,
        'sub_category': sub_cat,
        'page': page
    }

    return render(request, 'core/products.html', context)


def detail(request, pk):
    cat = Category.objects.all()
    obj = get_object_or_404(Product, pk=pk)
    related_obj = Product.objects.filter(SubCategory=obj.SubCategory).exclude(pk=obj.pk)[:8]

    ip = request.META.get('REMOTE_ADDR')

    if not View_Ips.objects.filter(ip=ip, Product=obj).exists():
        View_Ips.objects.create(Product=obj, ip=ip, Date=datetime.now(tz=timezone.utc))
    else:
        pass

    context = {
        'obj': obj,
        'related_obj': related_obj,
        'category': cat,
    }

    return render(request, 'core/product_details.html', context)


def category(request, category):
    cate = get_object_or_404(Category, Name=category)

    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    prod = cat_fun(cate)

    prod_paginator = Paginator(prod, 20)

    page_num = request.GET.get('page')

    page = prod_paginator.get_page(page_num)

    context = {
        'category': cat,
        'sub_category': sub_cat,
        'page': page
    }

    return render(request, 'core/products.html', context)


def sub_category(request, sub_category):
    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    prod = Product.objects.filter(SubCategory__Name=sub_category)

    prod_paginator = Paginator(prod, 20)

    page_num = request.GET.get('page')

    page = prod_paginator.get_page(page_num)

    context = {
        'category': cat,
        'sub_category': sub_cat,
        'page': page
    }

    return render(request, 'core/products.html', context)


def cat_fun(cat):
    sub_obj = get_list_or_404(SubCategory, Category=cat)
    return Product.objects.filter(SubCategory__in=sub_obj)


def blogs(request):
    cat = Category.objects.all()
    obj = Blog.objects.all()
    return render(request, 'core/blog.html', {'obj': obj, 'category': cat})


def blog_detail(request, name):
    cat = Category.objects.all()
    obj = get_object_or_404(Blog, Title=name)
    return render(request, 'core/blog_detail.html', {'obj': obj, 'category': cat})


def contact(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm

    context = {
        'category': cat,
        'form': form
    }
    return render(request, 'core/contact.html', context)


def about_us(request):
    obj = AboutUs.objects.get(id=1)
    return render(request, 'core/aboutus.html', {'obj': obj})
