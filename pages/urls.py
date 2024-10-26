# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("portfolio", views.portfolio_view, name='portfolio_view'),
]