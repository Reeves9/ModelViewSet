from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from quickstart import views as quickstart_views
# from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)
router.register(r'notes', quickstart_views.NoteViewSet)
# router.register(r'api',api_views.ResponseView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]