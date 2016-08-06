from django.conf.urls import url

from home.views import LandingView, IndexView

urlpatterns = [
    url(r'^landing/$', LandingView.as_view(), name='landing_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
]
