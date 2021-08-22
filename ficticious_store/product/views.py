from django.shortcuts import render

# Create your views here.

def index(request):
	"""Index View fot the virtual ficticious store"""

	context = {'keyword_01': 'value_01', 'keyword_02': 'value_02'}

	return render(request, 'index.html', context)

def product(request):

	return render(request, 'product.html')
