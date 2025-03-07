import enum

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "default"

class ReferenceEnum(enum.Enum):
    low = "low"
    normal = "normal"
    high = "high"

class PatientRelationEnum(enum.Enum):
    child = "child"
    dependent = "dependent"