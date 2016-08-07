import json

from django.views import View
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from disputes.models import Dispute
from disputes.category_questions import category_questions


@method_decorator(login_required, name='dispatch')
class DisputeView2(View):
    def get(self, request, alt_id=None):
        context = {
            'user': request.user
        }

        return render(request, 'dispute2.html', context)


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
        return render(request, 'dispute_list.html', context)


@method_decorator(login_required, name='dispatch')
class CreateDisputeView(View):
    def get(self, request):
        context = {
            'user': request.user,
            'categories': category_questions
        }
        return render(request, 'create_dispute.html', context)

    def post(self, request):
        cat_id = request.POST['category_selector'][0]

        if 'finish' in request.POST:
            # Save your json dump, if you want
            print(request.POST)
            return JsonResponse({'status': 'success'})

        else:
            with open('disputes/category_questions.json') as f:
                data = json.load(f)

            for d in data:
                if int(d['id']) == int(cat_id):
                    return JsonResponse(d)

            return JsonResponse()
