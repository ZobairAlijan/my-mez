from django.views import generic
from mysite.Main_page.models import Pages



class JobsPageView(generic.TemplateView):
    template_name = 'page/jobs.html'

    def get_context_data(self, **kwargs):
        context = super(JobsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'jobs')
        return context

