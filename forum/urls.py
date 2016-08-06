from django.conf.urls import url
from forum.views import index_view, resolve, dispute

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
    url(r'^dispute/?$', dispute, name='dispute'),
    url(r'^resolve/?$', resolve, name='resolve'),
]
