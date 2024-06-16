from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from dj_rest_auth.registration.views import RegisterView
from siteuser.models import User
urlpatterns = []
if settings.DEBUG:
	urlpatterns += [
		path("django/doc/", include("django.contrib.admindocs.urls")),
	]
urlpatterns += [
    path('accounts/', include('allauth.urls')),
    path('django/', admin.site.urls),
    path('user/', include('siteuser.urls')),
    path('explorer/', include('explorer.urls')),
    path('hijack/', include('hijack.urls')),
    path('search/', include('search.urls')),
    path('', include('home.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
# https://www.django-rest-framework.org/#example
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns += [
    path("api/", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include("dj_rest_auth.urls")),
    # path("api/register/", RegisterView.as_view(), name="register"),
]
