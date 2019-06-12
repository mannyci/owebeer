# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Beer
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Beer, AuthorAdmin)