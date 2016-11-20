from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.db.models import Q
import math

# Create your models here.
class UserManager(models.Manager):
    def getUsers(self, POST):
        if POST:
            page = int(POST['page'])
            name = POST['name']
            toDate = POST['toDate']
            fromDate = POST['fromDate']
        else:
            page = 1
            name = ''
            toDate = ''
            fromDate = ''
        if toDate == '':
            toDate = datetime.now()
        if fromDate == '':
            fromDate = datetime(1800, 01, 01)
        allUsers = User.objects.filter(Q(firstName__contains=name) | Q(lastName__contains=name)).filter(created_at__range=[fromDate, toDate])
        shownUsers = []
        count = 5
        while count > 0:
            if ((page * 5) - count) < len(allUsers):
                shownUsers.append(allUsers[((page * 5) - count)])
            count -= 1
        context = {
            'shownUsers': shownUsers,
            'pageRange': range(0, int(math.ceil(len(allUsers) / 5.0)))
        }
        return context


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
