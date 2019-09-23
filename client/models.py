from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class StreetAddress(models.Model):
	stret_name = models.CharField(max_length=200)
	suburb = models.CharField(max_length=200)
	postcode = models.IntegerField()
	state = models.CharField(max_length=200)

class Client(models.Model):
	client_name = models.CharField(max_length=200)
	address = models.ForeignKey('StreetAddress', on_delete=models.CASCADE, null=True)
	contact_name = models.CharField(max_length=200, blank=True)
	email_address = models.EmailField()
	phone_number = models.IntegerField(unique=True)

	def __str__(self):
		return self.client_name

	def get_absolute_url(self):
		return reverse('client_edit', kwargs={'pk': self.pk})
