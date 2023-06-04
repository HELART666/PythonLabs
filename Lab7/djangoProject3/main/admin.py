from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

User = get_user_model()

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
