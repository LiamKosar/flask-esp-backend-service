from api.database_objects import MaintenanceProcedure, Vehicle
from notifications.text_notifications import send_email


# Creates an email subject and body to notify a User of overdue MaintenanceProcedure(s) associated with a Vehicle
def notify_overdue_maintenance_procedures(vehicle:Vehicle, overdue_procedures: list[MaintenanceProcedure]):
    user_email = vehicle.user.email

    overdue_procedures_by_name = map(map_procedure_to_readable, overdue_procedures)

    # Creating the body of the email, where overdue procedures are listed out like:
    # Procedure 'Change Oil' is overdue by 1.0hrs
    body_result = "Hi, \n"
    for p in overdue_procedures_by_name:
        body_result += f"Procedure \"{p['name']}\" is overdue by {p['overdue_by']}hrs\n"
    
    subject = f"Overdue Maintenance on {vehicle.name}"    

    # Sends the email to the User that owns this Vehicle
    send_email(recipient=user_email, subject=subject, message_body=body_result)

# Maps an overdue MaintenanceProcedure to a readable format
def map_procedure_to_readable(procedure: MaintenanceProcedure):
    return {"name": procedure.name, "overdue_by": procedure.current_interval - procedure.interval}
