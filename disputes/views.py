from django.views import View
from django.shortcuts import render


class DisputeView(View):
    def get(self, request):
        return render(request, 'dispute.html', {})
