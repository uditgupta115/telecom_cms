from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def choices(cls):
        return ((tag.name, tag.value) for tag in cls)


class GenderEnum(BaseEnum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
