from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from semis.models import User_info


def index(request):
    context = {'hello': '123'}
    return render(request, 'semis/main.html', context)


def login(request):

    context = {'hello': '123'}
    return render(request, 'semis/login.html', context)