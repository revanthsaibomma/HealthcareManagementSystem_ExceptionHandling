"""
---------------------------------------------------------
File Name : appointment_module.py
Description : Appointment Management Module
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
=======
from logger_module import log_info, log_error, log_warning, log_exception
from validation_module import *

import mysql.connector
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

import mysql.connector

<<<<<<< HEAD
=======
# ---------------------------------------------------------
# Display Appointment Details
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def display_appointment(appointment):

    print("-" * 90)
    print(f"Appointment ID     : {appointment[0]}")
    print(f"Patient ID         : {appointment[1]}")
    print(f"Doctor ID          : {appointment[2]}")
    print(f"Appointment Date   : {appointment[3]}")
    print(f"Appointment Time   : {appointment[4]}")
    print(f"Status             : {appointment[5]}")
    print("-" * 90)
<<<<<<< HEAD

=======
# ---------------------------------------------------------
# Book Appointment
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def book_appointment():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== BOOK APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ").strip()

        validate_appointment_id(appointment_id)

        # Check Duplicate Appointment ID
        cursor.execute(
            "SELECT appointment_id FROM appointments WHERE appointment_id=%s",
            (appointment_id,)
        )

        if cursor.fetchone():

            print("\nAppointment ID already exists.")

<<<<<<< HEAD
            log_exception(f"Duplicate Appointment ID : {appointment_id}")

            return
=======
            log_error(f"Duplicate Appointment ID : {appointment_id}")

            return

        # -------------------------------
        # Validate Patient
        # -------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

        patient_id = input("Enter Patient ID : ").strip()

        validate_patient_id(patient_id)

        cursor.execute(
            "SELECT patient_name FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient is None:

            print("\nPatient Not Found.")

            return
<<<<<<< HEAD
=======

        # -------------------------------
        # Validate Doctor
        # -------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

        doctor_id = input("Enter Doctor ID : ").strip()

        validate_doctor_id(doctor_id)

        cursor.execute(
            """
            SELECT doctor_name,
                   availability_status
            FROM doctors
            WHERE doctor_id=%s
            """,
            (doctor_id,)
        )

        doctor = cursor.fetchone()

        if doctor is None:

            print("\nDoctor Not Found.")

            return

        if doctor[1] != "Available":

            print("\nDoctor is currently not available.")

            return
<<<<<<< HEAD
=======

        # -------------------------------
        # Appointment Date & Time
        # -------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

        appointment_date = input(
            "Enter Appointment Date (YYYY-MM-DD) : "
        ).strip()

        validate_date(appointment_date)

        appointment_time = input(
            "Enter Appointment Time (HH:MM:SS) : "
        ).strip()

        validate_time(appointment_time)

<<<<<<< HEAD
        cursor.execute(
            """
            SELECT appointment_id
            FROM appointments
            WHERE doctor_id=%s
            AND appointment_date=%s
            AND appointment_time=%s
            AND status='Scheduled'
            """,
            (
                doctor_id,
                appointment_date,
                appointment_time
            )
        )

        if cursor.fetchone():

            print("\nSelected Time Slot is already booked.")

            return

        sql = """
        INSERT INTO appointments
        (
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            status
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s
        )
        """

        values = (

=======
        # -------------------------------
        # Check Duplicate Slot
        # -------------------------------

        cursor.execute(
            """
            SELECT appointment_id
            FROM appointments
            WHERE doctor_id=%s
            AND appointment_date=%s
            AND appointment_time=%s
            AND status='Scheduled'
            """,
            (
                doctor_id,
                appointment_date,
                appointment_time
            )
        )

        if cursor.fetchone():

            print("\nSelected Time Slot is already booked.")

            return

        # -------------------------------
        # Insert Appointment
        # -------------------------------

        sql = """
        INSERT INTO appointments
        (
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            status
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s
        )
        """

        values = (

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            "Scheduled"

        )

        cursor.execute(sql, values)

        connection.commit()

        print("\nAppointment Booked Successfully.")

<<<<<<< HEAD
        log_application(
=======
        log_info(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            f"Appointment Booked : {appointment_id}"
        )

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
# View All Appointments
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def view_all_appointments():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT
                a.appointment_id,
                a.patient_id,
                p.patient_name,
                a.doctor_id,
                d.doctor_name,
                a.appointment_date,
                a.appointment_time,
                a.status
            FROM appointments a
            INNER JOIN patients p
                ON a.patient_id = p.patient_id
            INNER JOIN doctors d
                ON a.doctor_id = d.doctor_id
            ORDER BY a.appointment_date,
                     a.appointment_time
        """)

        appointments = cursor.fetchall()

        if len(appointments) == 0:

            print("\nNo Appointment Records Found.")
            return

        print("\n================ ALL APPOINTMENTS ================\n")

        for appointment in appointments:

            print("-" * 90)
            print(f"Appointment ID   : {appointment[0]}")
            print(f"Patient ID       : {appointment[1]}")
            print(f"Patient Name     : {appointment[2]}")
            print(f"Doctor ID        : {appointment[3]}")
            print(f"Doctor Name      : {appointment[4]}")
            print(f"Date             : {appointment[5]}")
            print(f"Time             : {appointment[6]}")
            print(f"Status           : {appointment[7]}")
            print("-" * 90)

        print(f"\nTotal Appointments : {len(appointments)}")

<<<<<<< HEAD
        log_application("Viewed All Appointments")
=======
        log_info("Viewed All Appointments")
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
# Search Appointment
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def search_appointment():

    connection = get_connection()

    if connection is None:

        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== SEARCH APPOINTMENT ==========")

        print("""
1. Search by Appointment ID
2. Search by Patient ID
3. Search by Doctor ID
4. Search by Appointment Date
5. Search by Status
""")

        choice = input("Enter your choice : ").strip()

<<<<<<< HEAD
=======
        # -----------------------------------------
        # Search by Appointment ID
        # -----------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

        if choice == "1":

            appointment_id = input("Enter Appointment ID : ").strip()

            validate_appointment_id(appointment_id)

            cursor.execute("""
                SELECT
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    status
                FROM appointments
                WHERE appointment_id=%s
            """, (appointment_id,))

<<<<<<< HEAD
=======
        # -----------------------------------------
        # Search by Patient ID
        # -----------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
        elif choice == "2":

            patient_id = input("Enter Patient ID : ").strip()

            validate_patient_id(patient_id)

            cursor.execute("""
                SELECT
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    status
                FROM appointments
                WHERE patient_id=%s
                ORDER BY appointment_date,
                         appointment_time
            """, (patient_id,))

<<<<<<< HEAD
=======
        # -----------------------------------------
        # Search by Doctor ID
        # -----------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
        elif choice == "3":

            doctor_id = input("Enter Doctor ID : ").strip()

            validate_doctor_id(doctor_id)

            cursor.execute("""
                SELECT
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    status
                FROM appointments
                WHERE doctor_id=%s
                ORDER BY appointment_date,
                         appointment_time
            """, (doctor_id,))

<<<<<<< HEAD
=======
        # -----------------------------------------
        # Search by Appointment Date
        # -----------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
        elif choice == "4":

            appointment_date = input(
                "Enter Appointment Date (YYYY-MM-DD) : "
            ).strip()

            # validate_date is provided by validation_module
            validate_date(appointment_date)

            cursor.execute("""
                SELECT
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    status
                FROM appointments
                WHERE appointment_date=%s
                ORDER BY appointment_time
            """, (appointment_date,))

<<<<<<< HEAD
=======
        # -----------------------------------------
        # Search by Status
        # -----------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
        elif choice == "5":

            print("\nAvailable Status")
            print("1. Scheduled")
            print("2. Completed")
            print("3. Cancelled")

            status_choice = input(
                "Enter Status Choice : "
            ).strip()

            status_dict = {
                "1": "Scheduled",
                "2": "Completed",
                "3": "Cancelled"
            }

            if status_choice not in status_dict:

                print("\nInvalid Status Choice.")
                return

            status = status_dict[status_choice]

            cursor.execute("""
                SELECT
                    appointment_id,
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    status
                FROM appointments
                WHERE status=%s
                ORDER BY appointment_date,
                         appointment_time
            """, (status,))

        else:

            print("\nInvalid Choice.")
            return

        appointments = cursor.fetchall()

        if len(appointments) == 0:

            print("\nNo Appointment Found.")

            log_warning("Appointment Search : No Records Found")

            return

        print("\n========== SEARCH RESULTS ==========\n")

        for appointment in appointments:

            display_appointment(appointment)

        print(f"Total Records Found : {len(appointments)}")

<<<<<<< HEAD
        log_application(
=======
        log_info(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            f"Appointment Search Successful ({len(appointments)} Record(s))"
        )

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
        log_exception(str(e)) # type: ignore
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

    finally:

        cursor.close()

        connection.close()

<<<<<<< HEAD
=======
# ---------------------------------------------------------
# Update Appointment Status
# ---------------------------------------------------------

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
def update_appointment_status():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== UPDATE APPOINTMENT STATUS ==========")

        appointment_id = input("Enter Appointment ID : ").strip()

        validate_appointment_id(appointment_id)

        cursor.execute("""
            SELECT appointment_id, status
            FROM appointments
            WHERE appointment_id=%s
        """, (appointment_id,))

        appointment = cursor.fetchone()

        if appointment is None:

            print("\nAppointment Not Found.")
            return

        print(f"\nCurrent Status : {appointment[1]}")

        print("\n1. Scheduled")
        print("2. Completed")
        print("3. Cancelled")

        choice = input("\nEnter New Status : ").strip()

        if choice == "1":
            status = "Scheduled"

        elif choice == "2":
            status = "Completed"

        elif choice == "3":
            status = "Cancelled"

        else:
            print("\nInvalid Choice.")
            return

        cursor.execute("""
            UPDATE appointments
            SET status=%s
            WHERE appointment_id=%s
        """, (status, appointment_id))

        connection.commit()

        print("\nAppointment Status Updated Successfully.")

<<<<<<< HEAD
        log_application(
=======
        log_info(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            f"Appointment Status Updated : {appointment_id} -> {status}"
        )

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
# Cancel Appointment
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def cancel_appointment():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== CANCEL APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ").strip()

        validate_appointment_id(appointment_id)

        cursor.execute("""
            SELECT
                appointment_id,
                patient_id,
                doctor_id,
                appointment_date,
                appointment_time,
                status
            FROM appointments
            WHERE appointment_id=%s
        """, (appointment_id,))

        appointment = cursor.fetchone()

        if appointment is None:

            print("\nAppointment Not Found.")
            return

        print("\nAppointment Details")
        display_appointment(appointment)

        # Already Cancelled

        if appointment[5] == "Cancelled":

            print("\nAppointment is already cancelled.")

<<<<<<< HEAD
            log_exception(
=======
            log_error(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
                f"Appointment Already Cancelled : {appointment_id}"
            )

            return

<<<<<<< HEAD
=======
        # Business Rule:
        # Completed appointments cannot be cancelled.

>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
        if appointment[5] == "Completed":

            print("\nCompleted Appointment cannot be cancelled.")

<<<<<<< HEAD
            log_exception(
=======
            log_error(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
                f"Cannot Cancel Completed Appointment : {appointment_id}"
            )

            return

        confirm = input(
            "\nAre you sure you want to cancel? (Y/N) : "
        ).strip().upper()

        if confirm != "Y":

            print("\nAppointment Cancellation Cancelled.")
            return

        cursor.execute("""
            UPDATE appointments
            SET status='Cancelled'
            WHERE appointment_id=%s
        """, (appointment_id,))

        connection.commit()

        print("\nAppointment Cancelled Successfully.")

<<<<<<< HEAD
        log_application(
=======
        log_info(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            f"Appointment Cancelled : {appointment_id}"
        )

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