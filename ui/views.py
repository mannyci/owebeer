# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.template import loader
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Count, Sum
from core.models import Beer, Team

from .utils import needs_setup
from .forms import SetupForm

class DashboardView(LoginRequiredMixin, DetailView):
    template = loader.get_template('index.html')

    def get(self, request):
        if needs_setup():
            return redirect('ui:setup')

        beers = Beer.objects.all().filter(user=request.user).aggregate(total=Sum('count'))
        print(beers)
        teams = Team.objects.count()
        recentBeers = Beer.objects.filter(user=request.user).order_by('-added_at')[:5]
        return HttpResponse(self.template.render({
            'beers': beers,
            'teams': teams,
            'recentBeers': recentBeers
        }, request))


class SetupView(View):
    template = loader.get_template('setup/setup.html')

    def get(self, request):
        if not needs_setup():
            return redirect('account:login')

        form = SetupForm(initial={
            'username': 'admin',
        })

        return HttpResponse(self.template.render({'form': form}, request))

    def post(self, request):
        form = SetupForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_superuser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            messages.success(request, 'Admin setup complete.')
            return redirect('account:login')
        return HttpResponse(self.template.render({'form': form}, request), status=400)
