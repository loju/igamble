from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from wallets.forms import DepositForm

import random


class IndexView(FormMixin, TemplateView):
    template_name = 'index.html'
    form_class = DepositForm

    def get_success_url(self):
        return redirect('board:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bonus_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.GET.get('spin'):
            active_wallet = self.request.user.get_active_wallet()
            active_wallet.spin()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('board:index')
