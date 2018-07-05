from django.conf.urls import url
from api.views import CompanyView, PersonView, CommonFriendsView

urlpatterns = [
    url(r'^company/(?P<pk>[0-9]+)$', CompanyView.as_view(), name='company-view'),
    url(r'^person/(?P<pk>[0-9]+)$', PersonView.as_view(), name='person-view'),
    url(
        r'^person/(?P<user_id>[0-9]+)/common-friends/(?P<comparison_user_id>[0-9]+)$',
        CommonFriendsView.as_view(),
        name='common-friends-view'
    ),
]