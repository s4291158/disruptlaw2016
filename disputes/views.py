import json

from django.views import View
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from disputes.models import Dispute
from disputes.category_questions import category_questions

from model_mommy import mommy


@method_decorator(login_required, name='dispatch')
class DisputeView2(View):
    def get(self, request, alt_id=None):
        context = {
            'user': request.user,
        }

        if alt_id:
            context['second_view'] = True

        return render(request, 'dispute2.html', context)

    def post(self, request):
        dispute = mommy.make(
            'Dispute',
            customer1=mommy.make(
                'Customer',
                baseuser=request.user
            )
        )

        context = {
            'dispute_alt_id': str(dispute.alt_id),
        }
        return JsonResponse(context)


@method_decorator(login_required, name='dispatch')
class DisputeView(View):
    def get(self, request, alt_id=None):
        context = {
            'user': request.user
        }
        if alt_id:
            context['second_view'] = True
            try:
                context['dispute'] = Dispute.objects.get(alt_id=alt_id)
            except:
                pass
        else:
            pass
        return render(request, 'dispute_list.html', context)


@method_decorator(login_required, name='dispatch')
class CreateDisputeView(View):
    def get(self, request, alt_id=None):
        context = {
            'user': request.user,
            'categories': category_questions
        }
        return render(request, 'create_dispute.html', context)

    def post(self, request, alt_id=None):
        # cat_id = request.POST['category_id'][0]

        # Save your json stuff
        print(request.POST)

        return JsonResponse({})
