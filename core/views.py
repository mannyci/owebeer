# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, Http404
from django.urls import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic.detail import View, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.db.models import Count
from .models import Team
from account.models import Account
from .forms import NewTeamForm, TeamUpdateForm


class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    form_class = NewTeamForm
    template_name = 'team/new.html'

    def get(self, request):
        return super(TeamCreate, self).get(request)

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.save()
        return super(TeamCreate, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Team addedd successfully')
        return reverse('ui:teams')


class TeamList(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'team/list.html'
    paginate_by = 2
    context_object_name = 'teams'

    def get(self, request, *args, **kwagrs):
        team = request.GET.get('team')
        self.object_list = self.get_queryset().order_by('id')
        if team:
            self.object_list = self.object_list.filter(team_id=team)
        context = self.get_context_data()
        return self.render_to_response(context)


class TeamDetail(LoginRequiredMixin, DetailView):
    model = Team
    template_name = 'team/details.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get_object(self, **kwargs):
        self.id = self.kwargs.get("id")
        if self.id is None:
            raise Http404
        return get_object_or_404(Team, id__iexact=self.id)


class TeamEdit(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamUpdateForm
    template_name = 'team/update.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'


    def get_object(self, **kwargs):
        self.id = self.kwargs.get("id")
        if self.id is None:
            raise Http404
        return get_object_or_404(Team, id__iexact=self.id)

    def get_success_url(self):
        messages.success(self.request, 'Team updated successfully')
        return reverse('ui:teams')


class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = 'team/delete.html'

    def get_object(self, **kwargs):
        self.name = self.kwargs.get("name")
        if self.name is None:
            raise Http404
        return get_object_or_404(Team, name__iexact=self.name)

    def get_success_url(self):
        messages.success(self.request, 'Host %s deleted successfully' % self.name)
        return reverse('ui:hosts')

class Members(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'member/details.html'
    context_object_name = 'teams'
    paginate_by = 2

    def get(self, request, *args, **kwagrs):
        team = request.GET.get('team')
        self.object_list = self.get_queryset().order_by('id')
        if team:
            self.object_list = self.object_list.filter(id=team)
        context = self.get_context_data()
        return self.render_to_response(context)
