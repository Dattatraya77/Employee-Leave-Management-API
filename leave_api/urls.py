from django.urls import path, include
from rest_framework import routers
from leave_api.views import EmployeeLeaveViewSet, CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'leaves', EmployeeLeaveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]