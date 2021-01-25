from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Meteor
from .forms import MeteorForm


def all_meteors(req):
    tmp = Meteor.objects.all()
    return render(req, 'all_meteors.html', {'meteors': tmp})


@login_required
def my_meteors(req):
    tmp = Meteor.objects.filter(posmatrac_id = req.user.id)
    return render(req, 'my_meteors.html', {'meteors': tmp})


@login_required
def add_meteor(req):
    if req.method == 'POST':
        forma = MeteorForm(req.POST)

        if forma.is_valid():
            m = Meteor(datum=forma.cleaned_data['datum'], vreme=forma.cleaned_data['vreme'], mesto=forma.cleaned_data['mesto'], magnituda=forma.cleaned_data['magnituda'], posmatrac=req.user)
            m.save()
            return render(req, 's_add.html')
        else:
            return render(req, 'add_meteors.html', {'form': forma})
    else:
        forma = MeteorForm()
        return render(req, 'add_meteors.html', {'form': forma})


def singin(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(req, user)
            tmp = Meteor.objects.all()
            return render(req, 'all_meteors.html', {'meteors': tmp})
    else:
        form = UserCreationForm()
    return render(req, 'singin.html', {'form': form})


@login_required
def meteor(req, id):
    tmp = get_object_or_404(Meteor, id=id)
    txt = ("m. id: " + str(tmp.id))
    return render(req, 'meteor.html', {'meteor': tmp, 'page_title': txt})


@login_required
def edit_meteor(req, id):
    if req.method == 'POST':
        forma = MeteorForm(req.POST)

        if forma.is_valid():
            m = Meteor.objects.get(id=id)
            if req.user == m.posmatrac:
                m.datum = forma.cleaned_data['datum']
                m.vreme = forma.cleaned_data['vreme']
                m.mesto = forma.cleaned_data['mesto']
                m.magnituda = forma.cleaned_data['magnituda']
                m.posmatrac = req.user
                m.save()
            return render(req, 's_edit.html')
        else:
            return render(req, 'edit_meteor.html', {'form': forma, 'id': id})
    else:
        tmp = get_object_or_404(Meteor, id=id)
        forma = MeteorForm(instance=tmp)
        return render(req, 'edit_meteor.html', {'form': forma, 'id': id})


@login_required
def del_meteor(req, id):
    m = get_object_or_404(Meteor, id=id)
    m.delete()
    return render(req, 's_del.html')