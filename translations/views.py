from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView
import json
from translations.transfer import Transfer
from translations.forms import TransferForm

# Create your views here.


class TranslateView(CreateView):
    form_class = TransferForm
    template_name = 'index.html'

    def get_form_kwargs(self):
        kwargs = super(TranslateView, self).get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        transfer = Transfer(obj.in_num)
        obj.out_num = transfer.transfer()
        obj.save()
        return JsonResponse({"result": obj.out_num})

    def form_invalid(self, form):
        return JsonResponse(dict(form.errors.items()), status=400)
