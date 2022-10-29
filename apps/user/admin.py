from django.contrib import admin

# Register your models here.
from apps.user.models import CustomUser

admin.site.register(CustomUser)
