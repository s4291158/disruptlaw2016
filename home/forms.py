from django.forms import ModelForm

from home.models import SignUp


class LandingForm(ModelForm):
    class Meta:
        model = SignUp
        exclude = ('id',)
