from django.conf.urls import url
from disputes.views import DisputeView

urlpatterns = [
    url(r'^dispute/$', DisputeView.as_view(), name='dispute_view'),
]
