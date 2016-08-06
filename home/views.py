from django.views import View
from django.shortcuts import render

from home.forms import LandingForm


class LandingView(View):
    def get(self, request):
        context = {
            'form': LandingForm()
        }
        return render(request, 'landing.html', context)

    def post(self, request):
        context = {}
        form = LandingForm(request.POST)
        if form.is_valid():
            form.save()
            context['message'] = "Success! We will notify you when we're live!"
        else:
            context['message'] = "This email address has already been submited."

        return render(request, 'landing.html', context)


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})
