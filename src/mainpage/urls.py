from django.urls import path

from mainpage.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view())
]
