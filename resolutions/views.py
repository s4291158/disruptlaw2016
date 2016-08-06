from django.views import View
from django.shortcuts import render


class ResolutionView(View):
    def get(self, request):
        return render(request, 'resolve.html', {})
