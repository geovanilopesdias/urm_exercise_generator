from random import choice
from enum import Enum

class UnitType(Enum):
    LENGTH = 'comprimento'
    TIME = 'tempo'
    SPEED = 'velocidade'
    ACCELERATION = 'aceleração'
    MASS = 'massa'
    VOLUME = 'volume'



class Unity:
    def __init__(self, n: str, s: str, t: 'UnitType', e: float):
        self.name = n
        self.symbol = s
        self.type = t
        self.si_eq = e  # Factor to multiply for in order to obtain the SI measure

    @staticmethod
    def convertToSI(value, unity: 'Unity'):
        return value * unity.si_eq

    @staticmethod
    def convertFromSI(value, unity: 'Unity'):
        return value / unity.si_eq

    def __str__(self, symbol_should_be_shown: bool = False):
        return f"{self.name} ({self.symbol})" if symbol_should_be_shown else f"{self.name}"
        
    

class UnitiesTable(Enum):
    METER = Unity('metro', 'm', UnitType.LENGTH, 1.0)
    MILES = Unity('milhas', 'mi', UnitType.LENGTH, 1_609.34)
    CENTIMETER = Unity('centímetro', 'cm', UnitType.LENGTH, 1e-2)
    KILOMETER = Unity('quilômetro', 'km', UnitType.LENGTH, 1e3)

    SECOND = Unity('segundo', 's', UnitType.TIME, 1)
    MINUTE = Unity('minuto', 'min', UnitType.TIME, 60)
    HOUR = Unity('hora', 'h', UnitType.TIME, 3_600)

    METER_PER_SECOND = Unity('metro por segundo', 'm/s', UnitType.SPEED, 1.0)
    KILOMETER_PER_HOUR = Unity('quilômetro por hora', 'km/h', UnitType.SPEED, 1/3.6)
    MILES_PER_HOUR = Unity('milha por hora', 'mi/h', UnitType.SPEED, .44704)

    def __str__(self):
        return self.value.__str__()
    
    @staticmethod
    def randomLengthUnity():
        unities = (UnitiesTable.METER, UnitiesTable.MILES, UnitiesTable.KILOMETER)
        return choice(unities).value

    @staticmethod
    def randomTimeUnity():
        unities = (UnitiesTable.SECOND, UnitiesTable.MINUTE, UnitiesTable.HOUR)
        return choice(unities).value

    @staticmethod
    def randomSpeedUnity():
        unities = (UnitiesTable.METER_PER_SECOND, UnitiesTable.KILOMETER_PER_HOUR, UnitiesTable.MILES_PER_HOUR)
        return choice(unities).value
