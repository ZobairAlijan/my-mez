__author__ = 'zobair'

import os
from django.shortcuts import get_object_or_404, render_to_response
from django.views import generic
from mysite.Main_page.models import Pages
from django.conf import settings
from mezzanine.utils.views import render


class IndexPageView(generic.TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'index')
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'page/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about')
        return context


class AboutBoardPageView(generic.TemplateView):
    template_name = 'page/about_board.html'

    def get_context_data(self, **kwargs):
        context = super(AboutBoardPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_board')
        return context

class PartnersPageView(generic.TemplateView):
    template_name = 'page/about_partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_partners')
        return context


class ServicePageView(generic.TemplateView):
    template_name = 'page/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'service')
        return context


class GetInvolvedPageView(generic.TemplateView):
    template_name = 'page/get_involved.html'

    def get_context_data(self, **kwargs):
        context = super(GetInvolvedPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'get-involved')
        return context


class StatsPageView(generic.TemplateView):
    template_name = 'page/stats_consulting.html'

    def get_context_data(self, **kwargs):
        context = super(StatsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'stats_consulting')
        return context


class MissionPageView(generic.TemplateView):
    template_name = 'page/about_mission.html'

    def get_context_data(self, **kwargs):
        context = super(MissionPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_mission')
        return context


class ApsPageView(generic.TemplateView):
    template_name = 'page/aps.html'

    def get_context_data(self, **kwargs):
        context = super(ApsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'aps')
        return context


class CommunitiesPageView(generic.TemplateView):
    template_name = 'page/communities.html'

    def get_context_data(self, **kwargs):
        context = super(CommunitiesPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'communities')
        return context


class InvolvedParticipatesPageView(generic.TemplateView):
    template_name = 'page/involved_participate.html'

    def get_context_data(self, **kwargs):
        context = super(InvolvedParticipatesPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'involved_participates')
        return context


class SponsorsPageView(generic.TemplateView):
    template_name = 'page/about_sponsors.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_sponsors')
        return context


class PrPageView(generic.TemplateView):

    def get(self, request, item):
        return render_to_response(os.path.join('page', 'pr', item) + '.html')