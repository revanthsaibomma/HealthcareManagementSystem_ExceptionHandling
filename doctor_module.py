"""
---------------------------------------------------------
File Name : doctor_module.py
Description : Doctor Management Module
---------------------------------------------------------
"""

from database_connection import get_connection
<<<<<<< HEAD
from logger_module import (
    log_application,
    log_exception,
    log_warning,
    log_debug,
    log_critical
)
from validation_module import *

import mysql.connector
=======
from logger_module import log_info, log_error
from validation_module import *

import mysql.connector


# ---------------------------------------------------------
# Display Doctor Details
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def display_doctor(doctor):

    print("-" * 70)
    print(f"Doctor ID            : {doctor[0]}")
    print(f"Doctor Name          : {doctor[1]}")
    print(f"Department           : {doctor[2]}")
    print(f"Consultation Fee     : ₹{doctor[3]}")
    print(f"Availability Status  : {doctor[4]}")
    print("-" * 70)
<<<<<<< HEAD
=======


# ---------------------------------------------------------
# Add Doctor
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def add_doctor():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== ADD DOCTOR ==========")

        doctor_id = input("Enter Doctor ID : ").strip()

        validate_doctor_id(doctor_id)

        cursor.execute(
            "SELECT doctor_id FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        if cursor.fetchone():

            print("\nDoctor ID already exists.")
<<<<<<< HEAD
            log_exception(f"Duplicate Doctor ID : {doctor_id}")
=======
            log_error(f"Duplicate Doctor ID : {doctor_id}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            return

        doctor_name = input("Enter Doctor Name : ").strip()

        validate_name(doctor_name)

        department = input("Enter Department : ").strip()

        validate_department(department)

        consultation_fee = float(
            input("Enter Consultation Fee : ")
        )

        validate_consultation_fee(consultation_fee)

        availability_status = input(
            "Availability (Available/Unavailable/On Leave) : "
        ).strip()

        validate_availability_status(availability_status)

        sql = """
        INSERT INTO doctors
        (
            doctor_id,
            doctor_name,
            department,
            consultation_fee,
            availability_status
        )
        VALUES
        (
            %s,%s,%s,%s,%s
        )
        """

        values = (

            doctor_id,
            doctor_name,
            department,
            consultation_fee,
            availability_status

        )

        cursor.execute(sql, values)

        connection.commit()

        print("\nDoctor Added Successfully.")

<<<<<<< HEAD
        log_application(f"Doctor Added : {doctor_id}")
=======
        log_info(f"Doctor Added : {doctor_id}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except ValueError as e:

        print("\nValidation Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except mysql.connector.Error as e:

        print("\nDatabase Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except Exception as e:

        print("\nUnexpected Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()
        connection.close()
<<<<<<< HEAD
=======
# ---------------------------------------------------------
# View All Doctors
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def view_all_doctors():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT
                doctor_id,
                doctor_name,
                department,
                consultation_fee,
                availability_status
            FROM doctors
            ORDER BY doctor_id
        """)

        doctors = cursor.fetchall()

        if len(doctors) == 0:

            print("\nNo Doctor Records Found.")
            return

        print("\n========== ALL DOCTORS ==========\n")

        for doctor in doctors:
            display_doctor(doctor)

        print(f"\nTotal Doctors : {len(doctors)}")

<<<<<<< HEAD
        log_application("Viewed All Doctors")
=======
        log_info("Viewed All Doctors")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except mysql.connector.Error as e:

        print("\nDatabase Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except Exception as e:

        print("\nUnexpected Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()
        connection.close()
<<<<<<< HEAD
=======


# ---------------------------------------------------------
# Search Doctor
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def search_doctor():

    connection = get_connection()

    if connection is None:

        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== SEARCH DOCTOR ==========")

        print("1. Doctor ID")
        print("2. Doctor Name")
        print("3. Department")
        print("4. Availability Status")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":

            doctor_id = input("Enter Doctor ID : ").strip()

            cursor.execute("""
                SELECT *
                FROM doctors
                WHERE doctor_id=%s
            """, (doctor_id,))

        elif choice == "2":

            doctor_name = input("Enter Doctor Name : ").strip()

            cursor.execute("""
                SELECT *
                FROM doctors
                WHERE doctor_name LIKE %s
            """, ("%" + doctor_name + "%",))

        elif choice == "3":

            department = input("Enter Department : ").strip()

            cursor.execute("""
                SELECT *
                FROM doctors
                WHERE department LIKE %s
            """, ("%" + department + "%",))

        elif choice == "4":

            status = input(
                "Enter Status (Available/Unavailable/On Leave) : "
            ).strip()

            cursor.execute("""
                SELECT *
                FROM doctors
                WHERE availability_status=%s
            """, (status,))

        else:

            print("\nInvalid Choice.")
            return

        doctors = cursor.fetchall()

        if len(doctors) == 0:

            print("\nNo Matching Doctor Found.")
            return

        print("\n========== SEARCH RESULT ==========\n")

        for doctor in doctors:
            display_doctor(doctor)

        print(f"\nTotal Records Found : {len(doctors)}")

<<<<<<< HEAD
        log_application("Doctor Search Performed")
=======
        log_info("Doctor Search Performed")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except mysql.connector.Error as e:

        print("\nDatabase Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except Exception as e:

        print("\nUnexpected Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()
        connection.close()
<<<<<<< HEAD
=======
# ---------------------------------------------------------
# Update Doctor
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def update_doctor():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== UPDATE DOCTOR ==========")

        doctor_id = input("Enter Doctor ID : ").strip()

        validate_doctor_id(doctor_id)

        cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        doctor = cursor.fetchone()

        if doctor is None:

            print("\nDoctor Not Found.")
            return

        print("\nCurrent Doctor Details")
        display_doctor(doctor)

        print("\nEnter New Details")

        doctor_name = input("Doctor Name : ").strip()
        validate_name(doctor_name)

        department = input("Department : ").strip()
        validate_department(department)

        consultation_fee = float(
            input("Consultation Fee : ")
        )
        validate_consultation_fee(consultation_fee)

        availability_status = input(
            "Availability (Available/Unavailable/On Leave) : "
        ).strip()

        validate_availability_status(availability_status)

        sql = """
        UPDATE doctors
        SET
            doctor_name=%s,
            department=%s,
            consultation_fee=%s,
            availability_status=%s
        WHERE doctor_id=%s
        """

        values = (
            doctor_name,
            department,
            consultation_fee,
            availability_status,
            doctor_id
        )

        cursor.execute(sql, values)

        connection.commit()

        print("\nDoctor Updated Successfully.")

<<<<<<< HEAD
        log_application(f"Doctor Updated : {doctor_id}")
=======
        log_info(f"Doctor Updated : {doctor_id}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except ValueError as e:

        print("\nValidation Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except mysql.connector.Error as e:

        print("\nDatabase Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except Exception as e:

        print("\nUnexpected Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()
        connection.close()

<<<<<<< HEAD
=======

# ---------------------------------------------------------
# Delete Doctor
# ---------------------------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
def delete_doctor():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== DELETE DOCTOR ==========")

        doctor_id = input("Enter Doctor ID : ").strip()

        validate_doctor_id(doctor_id)

        cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        doctor = cursor.fetchone()

        if doctor is None:

            print("\nDoctor Not Found.")
            return

        display_doctor(doctor)

        # Business Rule:
        # Do not allow deletion if doctor has
        # any scheduled appointments.

        cursor.execute(
            """
            SELECT appointment_id
            FROM appointments
            WHERE doctor_id=%s
            AND status='Scheduled'
            """,
            (doctor_id,)
        )

        if cursor.fetchone():

            print("\nCannot Delete Doctor.")
            print("Doctor has Scheduled Appointments.")

<<<<<<< HEAD
            log_exception(
=======
            log_error(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
                f"Delete Failed : Scheduled Appointment Exists ({doctor_id})"
            )

            return

        confirm = input("\nAre you sure? (Y/N) : ").strip().upper()

        if confirm != "Y":

            print("\nDeletion Cancelled.")
            return

        cursor.execute(
            "DELETE FROM doctors WHERE doctor_id=%s",
            (doctor_id,)
        )

        connection.commit()

        print("\nDoctor Deleted Successfully.")

<<<<<<< HEAD
        log_application(f"Doctor Deleted : {doctor_id}")
=======
        log_info(f"Doctor Deleted : {doctor_id}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except ValueError as e:

        print("\nValidation Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except mysql.connector.Error as e:

        print("\nDatabase Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    except Exception as e:

        print("\nUnexpected Error :", e)
<<<<<<< HEAD
        log_exception(str(e))
=======
        log_error(str(e))
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()
        connection.close()
        