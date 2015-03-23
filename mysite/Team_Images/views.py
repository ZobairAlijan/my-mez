from django.views import generic
from ..Team_Images.models import CropImageExample


class OurPictureView(generic.TemplateView):
    template_name = 'our_picture/index.html'

    def get_context_data(self, **kwargs):
        context = super(OurPictureView, self).get_context_data(**kwargs)
        context['images'] = CropImageExample.objects.all()
        return context

