from django.urls import path

from merch.views import MerchView

urlpatterns = [
    path('', MerchView.as_view())
]