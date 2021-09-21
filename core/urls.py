from django.urls import path
from .views import home, products, detail, blogs, blog_detail, category, sub_category, contact

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('products/', products, name='products'),
    path('blogs/', blogs, name='blogs'),
    path('blog_detail/<str:name>/', blog_detail, name='blog_detail'),
    path('category/<str:category>/', category, name='catgory'),
    path('sub_category/<str:sub_category>/', sub_category, name='sub_category'),
    path('contact/', contact, name='contact')
]
