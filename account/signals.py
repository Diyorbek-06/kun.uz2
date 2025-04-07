from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def manage_profile( instance, created):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
