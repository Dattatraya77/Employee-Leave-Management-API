from leave_api.models import EmployeeLeave, Company, Employee
from rest_framework import serializers


class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.CharField(source="company.name", read_only=True)
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeLeaveSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(
        source="employee.name",
        read_only=True
    )

    class Meta:
        model = EmployeeLeave
        fields = "__all__"
        read_only_fields = ("status",)