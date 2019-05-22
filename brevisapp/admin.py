from django.contrib import admin

from .models import ClientProfile, EditorProfile, EditingProject, Message

admin.site.register(ClientProfile)
admin.site.register(EditorProfile)
admin.site.register(EditingProject)
admin.site.register(Message)
