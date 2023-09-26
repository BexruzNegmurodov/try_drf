from django.urls import path
from .views import token

app_name = 'account'

urlpatterns = [
    path('token/', token, name='token')
]