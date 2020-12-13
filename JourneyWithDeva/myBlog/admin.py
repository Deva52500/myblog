from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import SiteLoc, User
admin.site.register(SiteLoc)
admin.site.register(User)
