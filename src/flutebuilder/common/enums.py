from enum import Enum


class InstrumentType(str, Enum):
    XIAO = "xiao"
    BANSURI = "bansuri"
    SHAKUHACHI = "shakuhachi"
    NEY = "ney"
    QUENA = "quena"
    KAVAL = "kaval"
    OTHER = "other"
