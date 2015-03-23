from django.shortcuts import get_object_or_404
from django.views import generic
from ..Team_Images.models import CropImageExample
from ..Main_page.models import Pages
from django.conf import settings


class HomepageView(generic.TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['images'] = CropImageExample.objects.all()
        context['page'] = Pages.objects.filter(slug = u'home')
        return context
