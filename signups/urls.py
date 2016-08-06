from django.conf.urls import url

from signups.views import LandingView

urlpatterns = [
    url(r'^landing/$', LandingView.as_view(), name='landing_view')

]
