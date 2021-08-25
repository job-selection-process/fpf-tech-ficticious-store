from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Product

# Create your views here.

def index(request):
	"""Index View fot the virtual ficticious store"""

	# print(request)

	# print(f'method: {request.method}')

	# print(f'headers: {request.headers}')

	# print(f"User-Agent: {request.headers['User-Agent']}")

	# print(f"User: {request.user}")

	logged: str = None

	if request.user == 'AnonymousUser':

		print('User not Logged')

		logged = 'Not Logged'

	else:

		print('User Logged')

		logged = 'Logged'

	# print(f"user.last_name: {request.user.last_name}")

	# print(f"user.email {request.user.email}")

	# print(f"user.is_staff (is part of the team - like superuser): {request.user.is_staff}")

	# print(dir(request))

	# print(dir(request.user))

	products = Product.objects.all()

	context = {
		'logged': logged,
		'products': products
	}

	return render(request, 'index.html', context)

def product(request, pk):

	# product_obj = Product.objects.get(pk=pk)

	product_obj = get_object_or_404(klass=Product, pk=pk)

	context = {

		'product': product_obj

	}

	return render(request, 'product.html', context)

def error404(request, exception):

	# render(request, '404.html')

	template = loader.get_template('404.html')

	return HttpResponse(
		content=template.render(),
		content_type='text/html; charset=utf8',
		status=404)

def error500(request):

	template = loader.get_template('500.html')	

	return HttpResponse(
		content=template.render(),
		content_type='text/html; charset=utf8', 
		status=500)