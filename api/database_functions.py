from pony.orm import select
import datetime
from notifications.overdue_maintenance_procedures import notify_overdue_maintenance_procedures
from api.database_objects import db, Device, MaintenanceProcedure, Vehicle, User

class DatabaseFunctions:
    
    # Returns the device associated with given mac_address
    # Outcomes:
    #   - Null if device doesn't exist
    #   - Device
    @classmethod
    def get_device_by_mac_address(this, mac_address: str):
        device = Device.get(mac_address=mac_address)
        return device

    # Checks if the given mac_address is associated with a Device
    @classmethod
    def contains_device_by_mac_address(this, mac_address: str):
        return Device.exists(mac_address = mac_address)
    
    # Checks if the given email is associated with a User
    @classmethod
    def contains_user_email_already(this, email: str):
        return User.exists(email=email)
    
    # Insert a new User with specified email
    @classmethod
    def insert_new_user_by_email(this, email: str):
        User(email = email)
        db.commit()

    # Returns the Vehicle associated with the given Device (if any)
    @classmethod
    def get_vehicle_by_device(this, device: Device):
        vehicle = Vehicle.get(device=device)
        return vehicle
    
    # Returns all maintenance procedures associated with given Vehicle (0 or many)
    @classmethod
    def get_maintenance_procedures_by_vehicle(this, vehicle: Vehicle):
        maintenance_procedures = select(m for m in MaintenanceProcedure if m.vehicle == vehicle)
        return maintenance_procedures
    
    # Updates the runtime of specified device ONLY IF there is a change from last update
    # Also:
    #   - If there is a Vehicle associated with Device, update its runtime
    #   - If there are MaintenanceProcedure(s) associated with Vehicle, update their runtime
    #   - If any updated MaintenanceProcedure exceeds set interval, email user with notification
    @classmethod
    def update_device_runtime(this, mac_address: str, runtime_hrs: float):

        device = this.get_device_by_mac_address(mac_address=mac_address)
        current_runtime = device.runtime
        runtime_difference = runtime_hrs - current_runtime
        
        # If there is no change from previous update
        if runtime_difference == 0:
            return
        
        # Update the value in the device object
        device.runtime = runtime_hrs
        device.date_updated = datetime.datetime.now().strftime("%Y-%m-%d")
        db.commit()

        # Getting the vehicle linked to this device
        vehicle = this.get_vehicle_by_device(device=device)
        
        # Potentially no vehicle connected
        if vehicle is None:
            return
        
        # Update the value in the vehicle object
        vehicle.runtime = vehicle.runtime + runtime_difference
        vehicle.date_updated = datetime.datetime.now().strftime("%Y-%m-%d")
        db.commit()

        maintenance_procedures = this.get_maintenance_procedures_by_vehicle(vehicle=vehicle)
        
        # Find all overdue MaintenanceProcedures
        overdue_procedures = []
        for procedure in maintenance_procedures:
            procedure.current_interval += runtime_difference
            
            # if exceeds interval, send alert
            if procedure.current_interval >= procedure.interval:
                overdue_procedures.append(procedure)

        db.commit()

        # If any overdue, email user
        # if len(overdue_procedures) > 0:
        #     notify_overdue_maintenance_procedures(vehicle=vehicle, overdue_procedures=overdue_procedures)


