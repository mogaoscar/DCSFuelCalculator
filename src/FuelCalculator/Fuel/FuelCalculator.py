from airframes.airframe import Airframe
from geometry.geometry import Vector

class FuelCalculator():
    def instantFuelFlow (airframe: Airframe, speed: float, altitude: float, flightRegime: int, step) -> float:
        '''
        Airframe is the airframe as it is at a given moment
        Speed in Mach.
        Altitude in feet ASL.
        flightRegime:
            - 0: Cruise
            - 1: Afterburner Cruise
            - 2: Climb
            - 3: Afterburner Climb
            - 4: Descent

        Returns a float containing the instant fuelFlow given the weight and drag index of the airframe, airframe fuelFlow data, the speed and altitude specified, and the type of flight regime specified.
        '''
        fuelFlow = 0.0
        weight = airframe.weight
        
        return fuelFlow
    
    def legFuelConsumed (airframe: Airframe, speed: float, altitude: float, weight) -> tuple[float, Airframe]:
        '''
        Speed in Mach?
        Altitude in feet ASL

        '''
        fuelConsumed = 0.0
        
        return fuelConsumed
    
    def tripFuelConsumed(airframe: Airframe, speed: float, altitude: float, weight, route: list[Vector]) -> tuple[float, Airframe]:
        '''
        Speed in Mach?
        Altitude in feet ASL

        '''
        fuelConsumed = 0.0
        
        return fuelConsumed
    
    def flightPlanFuelConsumed(airframe: Airframe, distanceHomeToAlternate, route: list[Vector]):
        FuelCalculator.tripFuelConsumed(airframe=airframe, speed=speed)
