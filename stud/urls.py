from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from stud.user.UserViewSet import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
