#from django.conf.urls import patterns, include, url
#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets, routers
from laundry.models import AuthUser, AuthGroup


from django.conf.urls import url, patterns, include
#from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers


#admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)



#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laundryshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 #   url(r'^admin/', include(admin.site.urls)),
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#)


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
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)