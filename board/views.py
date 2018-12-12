from django.views.generic import TemplateView

from wallets.forms import DepositForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bonus_form'] = DepositForm()
        return context
