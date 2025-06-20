from django.urls import path
from .views import registrar_tcu

urlpatterns = [
    path('registrar_tcu/', registrar_tcu, name='registrar_tcu'),
]