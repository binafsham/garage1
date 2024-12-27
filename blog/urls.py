from django.urls import path
from blog.views import index, contact, devosdetail, featuresdetail, carsdetail

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('devosdetail/<int:id>/', devosdetail, name='devosdetail'),
    path('featuresdetail/<int:id>/', featuresdetail, name='featuresdetail'),
    path('carsdetail/<int:id>/', carsdetail, name='carsdetail')
]
