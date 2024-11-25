import os
from pony.orm import Database, Required, db_session, PrimaryKey, Set, Optional, get, exists, select
import datetime
from notifications.overdue_maintenance_procedures import notify_overdue_maintenance_procedures
from api.database_objects import db, Device, MaintenanceProcedure, User, Vehicle

class DatabaseFunctions:
    
    # @classmethod
    # def get_runtime_difference(this, mac_address: str, runtime_hrs: float):
    #     device = Device.get(mac_address=mac_address)
    
    @classmethod
    def get_device_by_mac_address(this, mac_address: str):
        device = Device.get(mac_address=mac_address)
        return device
    
    @classmethod
    def contains_device_by_mac_address(this, mac_address: str):
        return Device.exists(mac_address = mac_address)
    
    @classmethod
    def get_vehicle_by_device(this, device: Device):
        vehicle = Vehicle.get(device=device)
        return vehicle
    
    @classmethod
    def get_maintenance_procedures_by_vehicle(this, vehicle: Vehicle):
        maintenance_procedures = select(m for m in MaintenanceProcedure if m.vehicle == vehicle)
        return maintenance_procedures
    
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
        
        overdue_procedures = []
        for procedure in maintenance_procedures:
            procedure.current_interval += runtime_difference
            
            # if exceeds interval, send alert
            if procedure.current_interval >= procedure.interval:
                overdue_procedures.append(procedure)

        db.commit()

        if len(overdue_procedures) > 0:
            notify_overdue_maintenance_procedures(vehicle=vehicle, overdue_procedures=overdue_procedures)


