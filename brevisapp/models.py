from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



class EditorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor')
    pending = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



class Message(models.Model):
    editingproject = models.ForeignKey('EditingProject', on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class EditingProject(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='projects')
    editor = models.ForeignKey(EditorProfile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=50, null=True, blank=True)
    orig_file = models.FileField(upload_to='textfile/', null=True, blank=True)
    orig_text = models.TextField(default='')
    description = models.CharField(max_length=500)
    turnaround = models.BooleanField(default='False')
    submit_date = models.DateTimeField(auto_now_add=True)
    edit_file = models.FileField(upload_to='textfile/', null=True, blank=True)
    edit_text = models.TextField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    final_date = models.DateTimeField(null=True, blank=True)
    word_count = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    submitted = models.BooleanField(default='False')


    def __str__(self):
        return self.client.user.username + ' - ' + self.name

    def due_date_str(self):
        if self.turnaround == False:
            two_days = datetime.timedelta(days=2)
            return self.submit_date + two_days
        else:
            four_hours = datetime.timedelta(hours=4)
            return self.submit_date + four_hours

    def turnaround_time(self):
        if self.turnaround == False:
            return "No"
        else:
            return "Yes"
