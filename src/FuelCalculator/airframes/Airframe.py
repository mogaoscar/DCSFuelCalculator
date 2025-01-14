from abc import ABC, abstractmethod, property

   
          
class Payload():
    def __init__(self, name: str, weight: float, maxFuel: float, fuel: float, isJettisonable: bool, ammo: int, maxAmmo: int) -> None:
        self.name = name

        self.weight = weight

        self.fuel = fuel
        self.maxFuel = maxFuel

        self.isJettisonable = isJettisonable
        self.isJettisoned = False

        self.maxAmmo = maxAmmo
        self.ammo = ammo
        return
    
    def Jettison(self) -> bool:
        if self.isJettisonable and not self.isJettisoned:
            self.weight = 0
            self.fuel = 0
            self.maxFuel = 0
            self.isJettisoned=True
            return True
        else:
            return False
        
class Pylon():
    def __init__(self, name: str, weight: float, isJettisonable: bool=None, payloads: list[Payload]=None) -> None:
        self.name = name

        self.weight = weight

        self.isJettisonable = isJettisonable
        self.isJettisoned = False

        self.payloads: list[Payload] = payload
        return
    
    def Jettison(self) -> bool:
        if self.isJettisonable and not self.isJettisoned:
            self.weight = 0
            self.fuel = 0
            self.maxFuel = 0
            self.isJettisoned=True
            return True
        else:
            return False


class Station():
    def __init__(self, name, payloads: list[Payload], emptyWeight: float, isJettisonable: bool) -> None:
        self.name = name

        self.payload: list[Payload] = payloads

        self.emptyWeight = emptyWeight
        self.weight = sum(payload.weight for payload in payloads)

        self.fuel = sum(payload.fuel for payload in payloads)
        self.maxFuel = sum(payload.maxFuel for payload in payloads)

        self.isJettisonable = isJettisonable
        return
    
class Airframe():
    def __init__(self, name, OEW: float, MTOW: float, stations: list[Station], maxInternalFuel: float, internalFuel: float) -> None:
        self.name: str = name
        self.stations: list[Station] = stations

        self.maxInternalFuel = maxInternalFuel
        self.maxExternalFuel = sum(station.maxfuel for station in self.stations)
        self.internalFuel = internalFuel
        self.externalFuel = sum(station.fuel for station in self.stations)
        self.fuel = self.internalFuel + self.externalFuel
        self.maxFuel = self.maxInternalFuel+self.maxExternalFuel

        self.OEW = OEW
        self.MTOW = MTOW
        self.weight = self.OEW+sum(station.weight for station in self.stations)+self.fuel

        self.dragIndex = self.calcDragIndex()
        return

    def calcdragIndex():
        pass
