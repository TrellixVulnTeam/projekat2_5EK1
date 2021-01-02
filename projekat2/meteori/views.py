from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Meteor


def all_meteors(req):
    tmp = Meteor.objects.all()
    return render(req, 'all_meteors.html', {'meteors': tmp})


@login_required
def my_meteors(req):
    tmp = Meteor.objects.all()
    return render(req,'my_meteors.html', {'meteors': tmp})

@login_required
def add_meteor(req):
    return render(req, 'add_meteors.html')


def singin(req):
    return render(req, 'singin.html')

@login_required
def meteor(req, id):
    tmp = get_object_or_404(Meteor, id=id)
    txt = ("m. id: " + str(tmp.id))
    return render(req, 'meteor.html', {'meteor': tmp, 'page_title': txt})