from django.forms import ModelForm

from signups.models import SignUp


class LandingForm(ModelForm):
    class Meta:
        model = SignUp
        exclude = ('id',)
