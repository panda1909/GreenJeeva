from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
import core


# Register your models here.
def create_action(subcategory):
    def action(modeladmin, request, queryset):
        queryset.update(SubCategory=subcategory)

    name = f'mark {subcategory}'
    return name, (action, name, f'Mark selected as {subcategory}')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductName', 'SKU', 'SubCategory', 'views')

    def get_actions(self, request):
        actions = dict(create_action(q) for q in SubCategory.objects.all())
        return actions


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Category')


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('Date', 'Title', 'get_tags')
    summernote_fields = ('Content',)


class ViewAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Date', 'ip')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'created_at')


class AboutUsAdmin(SummernoteModelAdmin):
    summernote_fields = ('Content',)

    def has_add_permission(self, request):
        # check if generally has add permission
        returnVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if returnVal and core.models.AboutUs.objects.exists():
            returnVal = False
        return returnVal

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(View_Ips, ViewAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
