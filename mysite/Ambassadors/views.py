from django.views import generic
from mysite.Ambassadors.models import Ambassadors


class AmbassadorsPageView(generic.TemplateView):
    template_name = 'page/ambassadors.html'

    def get_context_data(self, **kwargs):
        context = super(AmbassadorsPageView, self).get_context_data(**kwargs)
        context['ambassadors'] = Ambassadors.objects.all()
        return context
