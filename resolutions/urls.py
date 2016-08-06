from django.conf.urls import url

from resolutions.views import ResolutionView

urlpatterns = [
    url(r'^resolve/$', ResolutionView.as_view(), name='resolutions_view'),
]
