from django.contrib import admin
from .models import EmployeeLeave


@admin.register(EmployeeLeave)
class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "company", "leave_type", "start_date", "end_date", "reason", "status", "created_at", "updated_at"]

