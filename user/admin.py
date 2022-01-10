from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from user.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, UserProfile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserProfile
    list_display = ('email', 'is_staff', 'is_active','username')
    list_filter = ('email', 'is_staff', 'is_active','username')
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Profile)

