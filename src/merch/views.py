from django.shortcuts import render
from django.views import View

from merch.models import Merch


class MerchView(View):

    def get(self, request):
        return render(request, 'merch.html', {'merch': Merch.objects.all()})
