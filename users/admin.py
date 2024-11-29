from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, College

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Display fields in the admin list view
    list_display = ('id', 'username', 'email', 'college', 'location', 'birth_date', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'college__name', 'location')
    list_filter = ('is_staff', 'is_active', 'college')
    readonly_fields = ('date_joined', 'last_login')  # Fields that should not be editable

    # Fieldsets to group fields in the form view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'college', 'bio', 'location', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'college'),
        }),
    )

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('id', 'name', 'domain')
    search_fields = ('name', 'domain')
