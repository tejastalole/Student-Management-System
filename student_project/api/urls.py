from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import StudentViewset

router = DefaultRouter()
router.register(r'students', StudentViewset)


urlpatterns = [
    path('api/', include(router.urls))
]