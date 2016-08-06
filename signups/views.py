from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from signups.forms import LandingForm


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
            context['success'] = True
            context['message'] = "Success! We will notify you when we're live!"
        else:
            context['success'] = False
            context['message'] = "This email address has already been submited."

        return JsonResponse(context)
