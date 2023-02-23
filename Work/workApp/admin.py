from django.contrib import admin

# Register your models here.
from workApp.models import  User_Info ,Task,Bid


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone']

class TaskAdmin(admin.ModelAdmin):
    list_display=['user','document','description','duration','price','created_at']
class BidAdmin(admin.ModelAdmin):
    list_display=['task','user','price','timestamp']
    
admin.site.register(User_Info, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Bid, BidAdmin)
