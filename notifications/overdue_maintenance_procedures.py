from api.database_objects import db, Device, MaintenanceProcedure, User, Vehicle
from notifications.text_notifications import send_email



def notify_overdue_maintenance_procedures(vehicle:Vehicle, overdue_procedures: list[MaintenanceProcedure]):

    user_email = vehicle.user.email
    
    overdue_procedures_by_name = map(map_procedure_to_readable, overdue_procedures)

    
    body_result = "Hi, \n"
    
    for p in overdue_procedures_by_name:
        body_result += f"Procedure \"{p['name']}\" is overdue by {p['overdue_by']}hrs\n"
    
    subject = f"Overdue Maintenance on {vehicle.name}"    

    send_email(recipient=user_email, subject=subject, message_body=body_result)

def map_procedure_to_readable(procedure: MaintenanceProcedure):
    
    result = {
        "name": procedure.name,
        "overdue_by": procedure.current_interval - procedure.interval
    }

    return result