from rest_framework.response import Response
from leave_api.models import EmployeeLeave, Employee, Company
from rest_framework import viewsets
from leave_api.serializers import CompanySerializers, EmployeeSerializer, EmployeeLeaveSerializer
from rest_framework.decorators import action


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            if emp_serializer.data:
                return Response(emp_serializer.data)
            else:
                context = {
                    "message": "OOPS, Employee Not Found!"
                }
                return Response(context)
        except Exception as e:
            context = {
                "message": "OOPS, Company Not Found!"
            }
            return Response(context)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeLeaveViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLeave.objects.all()
    serializer_class = EmployeeLeaveSerializer

    def get_queryset(self):
        queryset = EmployeeLeave.objects.all()
        return queryset

    def perform_create(self, serializer):
        employee = serializer.validated_data["employee"]
        serializer.save(company=employee.company)

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        leave =  self.get_object()
        leave.status = "approved"
        leave.save()
        return Response({"message":"Leave Approved"})

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        leave = self.get_object()
        leave.status = "rejected"
        leave.save()
        return Response({"message":"Leave Rejected"})




