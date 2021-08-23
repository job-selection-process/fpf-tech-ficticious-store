from django.urls import path
from .views import index, product

urlpatterns = [
	path('', index, name='index'),	
	path('produtc/<int:pk>', product, name='product'),
]