from django.urls import path
from .views import subscribe_to_newsletter
from django.views.generic import TemplateView 

urlpatterns = [
    path('subscribe/', subscribe_to_newsletter, name='subscribe'),
    path('subscription-success/', TemplateView.as_view(template_name='subscription_success.html'), name='subscription_success'),
]