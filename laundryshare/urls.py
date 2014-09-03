from laundry.models import AuthUser, AuthGroup
from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers
from django.contrib import admin
from laundry.models import UserProfile

admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = AuthUser

class GroupViewSet(viewsets.ModelViewSet):
    model = AuthGroup


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/', 'laundry.views.user_profile')
)