from .models import User
from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_superuser",
    )
    search_fields = ("user_name", "email")


admin.site.register(User, UserAdmin)
