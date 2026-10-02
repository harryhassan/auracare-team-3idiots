3.	# AuraCare Health System Core
4.	APP_VERSION = "1.0.0"
5.	MODULES_ENABLED = []

def get_doctor_schedule(doctor_name):
    schedule = {
        "Dr. Khan": ["Monday", "Wednesday", "Friday"],
        "Dr. Ahmed": ["Tuesday", "Thursday"],
        "Dr. Ali": ["Monday", "Thursday", "Saturday"],
    }
    return schedule.get(doctor_name, "Doctor not found")
