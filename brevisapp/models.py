from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ClientProfile(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)

    # @receiver(post_save, sender=User)
    # def create_client_profile(sender, instance, created, **kwargs):
    #     if created:
    #         ClientProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_client_profile(sender, instance, **kwargs):
    #     instance.profile.save()

class EditorProfile(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    pending = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    # @receiver(post_save, sender=User)
    # def create_editor_profile(sender, instance, created, **kwargs):
    #     if created:
    #         EditorProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def create_editor_profile(sender, instance, **kwargs):
    #     instance.profile.save()

class EditingProject(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    editor = models.ForeignKey(EditorProfile, on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=50, null=True, blank=True)
    orig_file = models.FileField(upload_to='textfile/', null=True, blank=True)
    orig_text = models.TextField(default='')
    description = models.CharField(max_length=500)
    submit_date = models.DateTimeField(auto_now_add=True)
    edit_file = models.FileField(upload_to='textfile/', null=True, blank=True)
    edit_text = models.TextField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    final_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.orig_text

    def __str__(self):
        return self.description

    def __str__(self):
        return self.edit_text

    def __str__(self):
        return self.proj_name
