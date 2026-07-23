# 🏥 Healthcare Management System

A console-based **Healthcare Management System** developed using **Python** and **MySQL**. The project follows a modular architecture and implements CRUD operations, input validation, exception handling, logging, and report generation for efficient healthcare management.

---

## 📌 Features

### 👨‍⚕️ Patient Management
- Register Patient
- View All Patients
- Search Patient
- Update Patient
- Delete Patient

### 🩺 Doctor Management
- Add Doctor
- View All Doctors
- Search Doctor
- Update Doctor
- Delete Doctor

### 📅 Appointment Management
- Book Appointment
- View All Appointments
- Search Appointment
- Update Appointment Status
- Cancel Appointment

### 💳 Billing Management
- Generate Bill
- View All Bills
- Search Bill
- Update Payment Status

### 📊 Reports
- Patient Report
- Doctor Report
- Appointment Report
- Billing Report

---

## 🛠️ Technologies Used

- Python 3.x
- MySQL
- mysql-connector-python
- Object-Oriented Programming
- Exception Handling
- Logging
- Modular Programming

---

## 📂 Project Structure

```
HealthcareManagementSystem/

│── main.py
│── database_connection.py
│── validation_module.py
│── logger_module.py
│── patient_module.py
│── doctor_module.py
│── appointment_module.py
│── billing_module.py
│── report_module.py
│── healthcare_db.sql
│── requirements.txt
│── README.md

└── logs/
    ├── application_logs/
    └── exception_logs/
```

---

## 🗄️ Database Tables

- Patients
- Doctors
- Appointments
- Bills

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/revanthsaibomma/HealthcareManagementSystem_ExceptionHandling.git
```

### Navigate to Project

```bash
cd HealthcareManagementSystem_ExceptionHandling
```

### Install Required Package

```bash
pip install mysql-connector-python
```

### Create Database

Import

```
healthcare_db.sql
```

into MySQL.

### Configure Database

Update your MySQL credentials in

```
database_connection.py
```

Example

```python
host="localhost"
user="root"
password="Revanth@123"
database="healthcare_db"
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## 🔐 Validation

The project validates:

- Patient ID
- Doctor ID
- Appointment ID
- Bill ID
- Name
- Age
- Gender
- Contact Number
- Blood Group
- Department
- Consultation Fee
- Appointment Date
- Appointment Time
- Payment Status

---

## ⚠️ Exception Handling

The project handles:

- Validation Errors
- Database Errors
- Duplicate Records
- Invalid Input
- Unexpected Exceptions

---

## 📝 Logging

The application maintains separate logs for:

- Application Logs
- Exception Logs

Logs are automatically created inside the **logs/** folder.

---

## 📊 Reports

The application generates:

### Patient Report

- Total Patients
- Gender Statistics
- City Statistics
- Blood Group Statistics
- Disease Statistics
- Average Age

### Doctor Report

- Total Doctors
- Department Statistics
- Availability Status
- Consultation Fee Statistics

### Appointment Report

- Total Appointments
- Status Statistics
- Date-wise Report
- Doctor-wise Report
- Patient-wise Report

### Billing Report

- Total Bills
- Revenue
- Paid Amount
- Pending Amount
- Highest Bill
- Lowest Bill
- Average Bill

---

## 📷 Sample Modules

- Patient Management
- Doctor Management
- Appointment Management
- Billing Management
- Report Generation

---

## 🎯 Future Enhancements

- GUI using Tkinter
- Streamlit Web Application
- Email Notifications
- SMS Appointment Reminder
- PDF Bill Generation
- Dashboard and Charts

---

## 👨‍💻 Author

**Revanth Sai Bomma**

---

## 📜 License

This project is developed for educational and learning purposes.