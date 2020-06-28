from django.contrib import admin
from .models import Duser

# Register your models here.

class DuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'useremail')

admin.site.register(Duser, DuserAdmin)