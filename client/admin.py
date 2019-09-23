from django.contrib import admin
import adminactions.actions as actions

from .models import Client, StreetAddress

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
	pass

	list_display = ['id', 'client_name', 'contact_name', 'address', 'email_address', 'phone_number']
	ordering = ['client_name']

class StreetAddressAdmin(admin.ModelAdmin):
	list_display = ['stret_name', 'suburb', 'postcode', 'state']
	ordering = ['stret_name']

admin.site.register(Client, ClientAdmin)
admin.site.register(StreetAddress, StreetAddressAdmin)
