from django.contrib import admin
from .models import Profile, Activity, Joining

# Register your models here.
admin.site.register(Profile)
admin.site.register(Activity)
admin.site.register(Joining)
