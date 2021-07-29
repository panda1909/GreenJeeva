from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import View_Ips


@receiver(post_save, sender=View_Ips)
def update_view_count(sender, instance, created, **kwargs):
    if created:
        pro = instance.Product
        pro.views = pro.views + 1
        pro.save()
