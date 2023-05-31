from django.shortcuts import render
from django.utils import timezone
from django.views import View

from events.models import Events


class MainPageView(View):

    def get(self, request):

        return render(request, 'mainpage.html', {'events': Events.objects.filter(start_date__gte=timezone.now().date())})
