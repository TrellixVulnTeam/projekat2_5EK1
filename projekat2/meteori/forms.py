from django.forms import ModelForm
from .models import Meteor

class MeteorForm(ModelForm):
    class Meta:
        model = Meteor
        fields = ['datum', 'vreme', 'mesto', 'magnituda']