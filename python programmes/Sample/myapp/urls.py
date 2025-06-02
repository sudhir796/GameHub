from django.urls import path
from .views import features
from .views import home
urlpatterns=[
    path('form/',home,name='home'),
    path('features/',features,name='features')
]