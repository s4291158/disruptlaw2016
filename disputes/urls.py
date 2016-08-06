from django.conf.urls import url
from disputes.views import DisputeView, CreateDisputeView

urlpatterns = [
    url(
        r'^dispute/?$',
        CreateDisputeView.as_view(),
        name='create_dispute_view'
    ),
    url(
        r'^dispute/(?P<alt_id>[0-9]+)/?$',
        DisputeView.as_view(),
        name='dispute_view'
    ),
    url(
        r'^disputes/?$',
        DisputeView.as_view(),
        name='dispute_view'
    ),
]
