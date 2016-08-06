from django.views import View
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from disputes.models import Dispute
from disputes.category_questions import category_questions


@method_decorator(login_required, name='dispatch')
class DisputeView(View):
    def get(self, request, alt_id=None):
        context = {
            'user': request.user
        }
        if alt_id:
            try:
                context['dispute'] = Dispute.objects.get(alt_id=alt_id)
            except Dispute.DoesNotExist:
                return Http404
        else:
            pass
        return render(request, '', context)


@method_decorator(login_required, name='dispatch')
class CreateDisputeView(View):
    def get(self, request):
        context = {
            'user': request.user,
            'categories': category_questions
        }
        return render(request, 'create_dispute.html', context)
