from django import forms
from django.db.models import Q
from django.forms import ModelForm
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect

from .models import Client

class HomePageView(TemplateView):

	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['clients'] = Client.objects.all()
		return context

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = ['client_name', 'email_address', 'phone_number']

def client_list(request):
	orderby_name = request.GET.get('orderby_name', '')
	orderby_email = request.GET.get('orderby_email', '')
	orderby_phone_number = request.GET.get('orderby_phone_number', '')
	orderby_suburb = request.GET.get('orderby_suburb', '')
	clients = Client.objects.all()

	if(orderby_name == 'desc'):
		clients = clients.order_by('-client_name')
	elif(orderby_name == 'asc'):
		clients = clients.order_by('client_name')

	if(orderby_email == 'desc'):
		clients = clients.order_by('-email_address')
	elif(orderby_email == 'asc'):
		clients = clients.order_by('email_address')

	if(orderby_phone_number == 'desc'):
		clients = clients.order_by('-phone_number')
	elif(orderby_phone_number == 'asc'):
		clients = clients.order_by('phone_number')

	if(orderby_suburb == 'desc'):
		clients = clients.order_by('-address__suburb')
	elif(orderby_suburb == 'asc'):
		clients = clients.order_by('address__suburb')


	context = {
		'clients': clients,
		'orderby_name': orderby_name,
		'orderby_email': orderby_email,
		'orderby_phone_number': orderby_phone_number,
		'orderby_suburb': orderby_suburb,
	}
	return render(request, 'home.html', context)

def client_new(request, template_name='client_form.html'):
	form = ClientForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('client_list')
	return render(request, template_name, {'form':form})

def client_update(request, pk, template_name='client_form.html'):
	client= get_object_or_404(Client, pk=pk)
	form = ClientForm(request.POST or None, instance=client)
	if form.is_valid():
		form.save()
		return redirect('client_list')
	return render(request, template_name, {'form':form})

def client_search(request):
	query_search = request.GET.get('q','')
	searchby = request.GET.get('order_by', '')
	if query_search:
		if searchby == 'client_name':
			queryset = (Q(client_name__icontains=query_search))
		elif searchby == 'email_address':
			queryset = (Q(email_address__icontains=query_search))
		elif searchby == 'phone_number':
			queryset = (Q(phone_number__icontains=query_search))
		elif searchby == 'suburb':
			queryset = (Q(address__suburb__icontains=query_search))
		search_result = Client.objects.filter(queryset).distinct()
	else:
	   search_result = []
	return render(request, 'client_search.html', {'search_result':search_result, 'query_search':query_search})
