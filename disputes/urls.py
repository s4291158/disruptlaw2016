from django.conf.urls import url
from disputes.views import DisputeView, DisputeListView

urlpatterns = [
    url(r'^dispute/?$', DisputeView.as_view(), name='dispute_view'),
    url(r'^dispute/list/?$', DisputeListView.as_view(), name='dispute_list_view'),
]
