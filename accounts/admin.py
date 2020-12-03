from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Business, Customer, Auto, GeeksModel, Continent, Country, Location

# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer_id')
    readonly_fields = ['customer_id']


admin.site.register(User, UserAdmin)
admin.site.register(Business)
admin.site.register(Customer)
admin.site.register(Auto)
admin.site.register(GeeksModel, GeeksModelAdmin)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location)
