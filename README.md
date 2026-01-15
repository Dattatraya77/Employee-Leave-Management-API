🧑‍💼 Employee Leave Management API

A RESTful API built using Django Rest Framework (DRF) to manage:

Companies

Employees

Employee Leave Requests

Leave Approval / Rejection Workflow

This API is suitable for HR systems, internal tools, and multi-company employee management platforms.

🚀 Tech Stack

Python

Django

Django Rest Framework

SQLite / PostgreSQL (configurable)

📦 Models Overview
1️⃣ Company

Stores company-level information

One company → many employees

One company → many leave requests

2️⃣ Employee

Belongs to a company

Can request multiple leaves

3️⃣ EmployeeLeave

Leave request for an employee

Auto-linked to company

Supports approval & rejection

🔗 API Base URL
http://127.0.0.1:8000/api/

🔐 Authentication

❗ Currently no authentication is implemented
(Recommended: JWT / Token Authentication for production)

📌 API Endpoints
🏢 Company APIs
➤ Create Company

POST

/api/companies/


Request Body

{
    "name": "TechCorp",
    "location": "Pune",
    "about": "Software Development Company",
    "company_type": "startup",
    "active": true
}


Response

{
    "company_id": 1,
    "name": "TechCorp",
    "location": "Pune",
    "about": "Software Development Company",
    "company_type": "startup",
    "created_at": "2026-01-15T10:00:00Z",
    "updated_at": "2026-01-15T10:00:00Z",
    "active": true
}

➤ List Companies

GET

/api/companies/

➤ Get Company Details

GET

/api/companies/{company_id}/

➤ Get Employees of a Company

GET

/api/companies/{company_id}/employees/


Response

[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@techcorp.com",
    "employee_position": "senior",
    "company": 1,
    "company_name": "TechCorp"
  }
]


👨‍💼 Employee APIs
➤ Create Employee

POST

/api/employees/


Request Body

{
    "name": "Rahul Sharma",
    "email": "rahul@techcorp.com",
    "address": "Pune, India",
    "phone": "+919876543210",
    "about": "Backend Developer",
    "employee_position": "senior",
    "company": 1,
    "active": true
}


Response

{
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@techcorp.com",
    "employee_position": "senior",
    "company": 1,
    "company_name": "TechCorp",
    "active": true
}

➤ List Employees

GET

/api/employees/

➤ Get Employee Details

GET

/api/employees/{employee_id}/

📝 Employee Leave APIs
➤ Apply for Leave

POST

/api/leaves/


Request Body

{
    "employee": 1,
    "leave_type": "sick",
    "start_date": "2026-01-20",
    "end_date": "2026-01-22",
    "reason": "Fever and rest"
}


🔹 Company is auto-assigned from employee

Response

{
    "id": 1,
    "employee": 1,
    "employee_name": "Rahul Sharma",
    "company": 1,
    "leave_type": "sick",
    "start_date": "2026-01-20",
    "end_date": "2026-01-22",
    "reason": "Fever and rest",
    "status": "pending"
}

➤ List All Leaves

GET

/api/leaves/

➤ Get Leave Details

GET

/api/leaves/{leave_id}/

➤ Approve Leave

POST

/api/leaves/{leave_id}/approve/


Response

{
  "message": "Leave Approved"
}

➤ Reject Leave

POST

/api/leaves/{leave_id}/reject/


Response

{
  "message": "Leave Rejected"
}

🔄 Leave Status Flow
PENDING → APPROVED
        → REJECTED

🧪 Example Use Case Flow

Create Company

Add Employees under Company

Employee applies for leave

HR/Admin approves or rejects leave

⚙️ Installation & Setup
git clone https://github.com/yourusername/employee-leave-management-api.git
cd employee-leave-management-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

👨‍💻 Author

Dattatraya Walunj

Senior Django Backend Developer
