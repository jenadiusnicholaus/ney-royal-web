from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    image = models.FileField(upload_to='profile_files', null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=20, null=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    region = models.CharField(max_length=15, null=True, blank=True)
    district = models.CharField(max_length=15, null=True, blank=True)
    ward = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.user.email)

    def imageUrl(self):
        if self.image:
            return self.image.url
        return None


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=User)
