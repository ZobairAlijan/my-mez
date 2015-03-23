from django.views import generic
from mysite.news.models import News


class NewsPageView(generic.TemplateView):
    template_name = 'page/news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsPageView, self).get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context