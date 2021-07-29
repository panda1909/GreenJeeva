from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Product, Category, SubCategory, Blog, View_Ips


# Create your views here.

def home(request):
    dot = datetime.now(tz=timezone.utc)
    d = timedelta(days=14)
    sub = dot - d

    category = Category.objects.all()
    popular_prods = Product.objects.all().order_by('views')[:8]
    trending_prods_id = View_Ips.objects.filter(Date__range=[sub, dot]).values('Product_id')
    trending_prods = Product.objects.filter(pk__in=trending_prods_id)

    context = {
        'category': category,
        'popular_products': popular_prods,
        'trending_products': trending_prods
    }

    return render(request, 'landing.html', context)


def products(request):
    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    prod = Product.objects.all()

    context = {
        'category': cat,
        'sub_category': sub_cat,
        'product': prod
    }

    return render(request, 'core/products.html', context)


def detail(request, pk):
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
    }

    return render(request, 'core/product_details.html', context)


def Blogs(request):
    obj = Blog.objects.all()

