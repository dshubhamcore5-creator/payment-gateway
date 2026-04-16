
from django.urls import path
from .views import create_order

urlpatterns = [
    path('create/<int:plan_id>/', create_order),
]
