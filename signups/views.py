from django.views import View
from django.shortcuts import render

from signups.forms import LandingForm


class LandingView(View):
    def get(self, request):
        return render(request, 'landing.html', {})

    def post(self, request):
        form = LandingForm(request.POST)
        if form.is_valid():
            form.save()
