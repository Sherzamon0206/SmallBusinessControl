from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('registration/', registerView, name='register'),
    path("freeadvice/", BlogPageView, name="blogpage"),
    path('freeadvice/<slug:slug>/', BlogDetailView, name='blog_detail'),
    path('invoice/', invoiceView, name='invoice'),
    path('', homeView, name = 'home'),
    path('tax_calculator/', CalculatorView, name = 'calculator_page'),
]