from django.contrib import admin
from .models import Profile, Activity, Joining, Comment, Deleted, Banneduser

# Register your models here.
admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Joining)
admin.site.register(Comment)
admin.site.register(Deleted)
admin.site.register(Banneduser)
