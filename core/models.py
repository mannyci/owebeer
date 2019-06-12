# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from account.models import Account


class Beer(models.Model):
    class Meta:
        db_table = 'beer_count'

    count = models.IntegerField(default=0, verbose_name='Count of beer per user')
    user = models.ForeignKey(Account, related_name='link_to_the_person')
    added_by = models.ForeignKey(Account, related_name='link_to_the_person_added')
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.count)

class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='link_to_the_person_created')
    members = models.ManyToManyField(Account)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ui:teamdetail", kwargs={"id": self.id})
