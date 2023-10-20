from django.contrib import admin
from userauths.models import User

# from import_export.admin import ImportExportModelAdmin 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

admin.site.register(User, UserAdmin)