from django.contrib import admin
from .models import user
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=('id','name','email','password','created_at')