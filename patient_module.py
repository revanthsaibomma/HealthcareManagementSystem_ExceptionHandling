"""
---------------------------------------------------------
File Name : patient_module.py
Description : Patient Management Module
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

def display_patient(patient):

    print("-" * 80)
    print(f"Patient ID      : {patient[0]}")
    print(f"Patient Name    : {patient[1]}")
    print(f"Age             : {patient[2]}")
    print(f"Gender          : {patient[3]}")
    print(f"Contact Number  : {patient[4]}")
    print(f"City            : {patient[5]}")
    print(f"Blood Group     : {patient[6]}")
    print(f"Disease         : {patient[7]}")
    print("-" * 80)
=======
from logger_module import log_info, log_error
from validation_module import *

import mysql.connector


# ---------------------------------------------------------
# Display Patient Details
# ---------------------------------------------------------

def display_patient(patient):

    print("-" * 80)
    print(f"Patient ID      : {patient[0]}")
    print(f"Patient Name    : {patient[1]}")
    print(f"Age             : {patient[2]}")
    print(f"Gender          : {patient[3]}")
    print(f"Contact Number  : {patient[4]}")
    print(f"City            : {patient[5]}")
    print(f"Blood Group     : {patient[6]}")
    print(f"Disease         : {patient[7]}")
    print("-" * 80)


# ---------------------------------------------------------
# Register Patient
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def register_patient():

    connection = get_connection()

    if connection is None:
        print("\nDatabase connection failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== Register Patient ==========")

        patient_id = input("Enter Patient ID : ").strip()

        validate_patient_id(patient_id)

        cursor.execute(
            "SELECT patient_id FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        if cursor.fetchone():

            print("\nPatient ID already exists.")
<<<<<<< HEAD
            log_exception(f"Duplicate Patient ID : {patient_id}")
=======
            log_error(f"Duplicate Patient ID : {patient_id}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            return

        patient_name = input("Enter Patient Name : ").strip()
        validate_name(patient_name)

        age = int(input("Enter Age : "))
        validate_age(age)

        gender = input("Enter Gender (Male/Female/Other) : ").strip()
        validate_gender(gender)

        contact_number = input("Enter Contact Number : ").strip()
        validate_contact_number(contact_number)

        cursor.execute(
            "SELECT contact_number FROM patients WHERE contact_number=%s",
            (contact_number,)
        )

        if cursor.fetchone():

            print("\nContact Number already exists.")
<<<<<<< HEAD
            log_exception(f"Duplicate Contact Number : {contact_number}")
=======
            log_error(f"Duplicate Contact Number : {contact_number}")
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
            return

        city = input("Enter City : ").strip()
        validate_city(city)

        blood_group = input("Enter Blood Group : ").strip()
        validate_blood_group(blood_group)

        disease = input("Enter Disease : ").strip()
        validate_disease(disease)

        sql = """
        INSERT INTO patients
        (
            patient_id,
            patient_name,
            age,
            gender,
            contact_number,
            city,
            blood_group,
            disease
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        values = (
            patient_id,
            patient_name,
            age,
            gender,
            contact_number,
            city,
            blood_group,
            disease
        )

        cursor.execute(sql, values)

        connection.commit()

        print("\nPatient Registered Successfully.")

<<<<<<< HEAD
        log_application(f"Patient Registered : {patient_id}")
=======
        log_info(f"Patient Registered : {patient_id}")
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
# View All Patients
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def view_all_patients():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT
                patient_id,
                patient_name,
                age,
                gender,
                contact_number,
                city,
                blood_group,
                disease
            FROM patients
            ORDER BY patient_id
        """)

        patients = cursor.fetchall()

        if len(patients) == 0:
            print("\nNo Patient Records Found.")
            return

        print("\n========== ALL PATIENTS ==========\n")

        for patient in patients:
            display_patient(patient)

        print(f"\nTotal Patients : {len(patients)}")

<<<<<<< HEAD
        log_application("Viewed All Patients")
=======
        log_info("Viewed All Patients")
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
# Search Patient
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def search_patient():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== SEARCH PATIENT ==========")

        print("1. Patient ID")
        print("2. Patient Name")
        print("3. Contact Number")
        print("4. City")
        print("5. Blood Group")
        print("6. Disease")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":

            patient_id = input("Enter Patient ID : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE patient_id=%s
            """, (patient_id,))

        elif choice == "2":

            patient_name = input("Enter Patient Name : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE patient_name LIKE %s
            """, ("%" + patient_name + "%",))

        elif choice == "3":

            contact = input("Enter Contact Number : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE contact_number=%s
            """, (contact,))

        elif choice == "4":

            city = input("Enter City : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE city LIKE %s
            """, ("%" + city + "%",))

        elif choice == "5":

            blood = input("Enter Blood Group : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE blood_group=%s
            """, (blood,))

        elif choice == "6":

            disease = input("Enter Disease : ").strip()

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE disease LIKE %s
            """, ("%" + disease + "%",))

        else:

            print("\nInvalid Choice.")
            return

        patients = cursor.fetchall()

        if len(patients) == 0:

            print("\nNo Matching Patient Found.")
            return

        print("\n========== SEARCH RESULT ==========\n")

        for patient in patients:
            display_patient(patient)

        print(f"\nTotal Records Found : {len(patients)}")

<<<<<<< HEAD
        log_application("Patient Search Performed")
=======
        log_info("Patient Search Performed")
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
# Update Patient
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def update_patient():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== UPDATE PATIENT ==========")

        patient_id = input("Enter Patient ID : ").strip()

        validate_patient_id(patient_id)

        cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient is None:

            print("\nPatient Not Found.")
            return

        print("\nCurrent Patient Details")
        display_patient(patient)

        print("\nEnter New Details")

        patient_name = input("Patient Name : ").strip()
        validate_name(patient_name)

        age = int(input("Age : "))
        validate_age(age)

        gender = input("Gender (Male/Female/Other) : ").strip()
        validate_gender(gender)

        contact_number = input("Contact Number : ").strip()
        validate_contact_number(contact_number)

        cursor.execute(
            """
            SELECT patient_id
            FROM patients
            WHERE contact_number=%s
            AND patient_id<>%s
            """,
            (contact_number, patient_id)
        )

        if cursor.fetchone():

            print("\nContact Number already exists.")
            return

        city = input("City : ").strip()
        validate_city(city)

        blood_group = input("Blood Group : ").strip()
        validate_blood_group(blood_group)

        disease = input("Disease : ").strip()
        validate_disease(disease)

        sql = """
        UPDATE patients
        SET
            patient_name=%s,
            age=%s,
            gender=%s,
            contact_number=%s,
            city=%s,
            blood_group=%s,
            disease=%s
        WHERE patient_id=%s
        """

        values = (
            patient_name,
            age,
            gender,
            contact_number,
            city,
            blood_group,
            disease,
            patient_id
        )

        cursor.execute(sql, values)

        connection.commit()

        print("\nPatient Updated Successfully.")

<<<<<<< HEAD
        log_application(f"Patient Updated : {patient_id}")
=======
        log_info(f"Patient Updated : {patient_id}")
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
# Delete Patient
# ---------------------------------------------------------
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f

def delete_patient():

    connection = get_connection()

    if connection is None:
        print("\nDatabase Connection Failed.")
        return

    cursor = connection.cursor()

    try:

        print("\n========== DELETE PATIENT ==========")

        patient_id = input("Enter Patient ID : ").strip()

        validate_patient_id(patient_id)

        cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient is None:

            print("\nPatient Not Found.")
            return

        display_patient(patient)

        # Business Rule:
        # Do not allow deletion if any Scheduled appointment exists.

        cursor.execute(
            """
            SELECT appointment_id
            FROM appointments
            WHERE patient_id=%s
            AND status='Scheduled'
            """,
            (patient_id,)
        )

        if cursor.fetchone():

            print("\nCannot Delete Patient.")
            print("Scheduled Appointment Exists.")

<<<<<<< HEAD
            log_exception(
=======
            log_error(
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
                f"Delete Failed : Scheduled Appointment Exists ({patient_id})"
            )

            return

        confirm = input("\nAre you sure? (Y/N) : ").strip().upper()

        if confirm != "Y":

            print("\nDeletion Cancelled.")
            return

        cursor.execute(
            "DELETE FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        connection.commit()

        print("\nPatient Deleted Successfully.")

<<<<<<< HEAD
        log_application(f"Patient Deleted : {patient_id}")
=======
        log_info(f"Patient Deleted : {patient_id}")
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