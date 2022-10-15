from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from .models import PushUserModel, PushGroupModel, UserGroupModel, PushMessageModel, PushToGroupModel

# Register your models here.

class UserGroupModelTabularInline(admin.TabularInline):
    model = UserGroupModel
    extra = 0

@admin.register(PushUserModel)
class PushUserModelAdmin(admin.ModelAdmin):
    inlines = [UserGroupModelTabularInline]
    list_display = ['identifier']


@admin.register(PushGroupModel)
class PushGroupModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(PushMessageModel)
class PushMessageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(PushToGroupModel)
class PushToGroupModelAdmin(admin.ModelAdmin):
    list_display = ['pushGroup', 'pushMessage', 'sendDate']

    change_form_template = "pushUser/admin/pushToGroup.html" 

    def response_change(self, request, obj):
        if 'sendNotif' in request.POST:
            obj.sendNotif()
        return super().response_change(request, obj)
