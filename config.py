from os import getenv

ENV = True

if ENV:
    TOKEN1 = getenv("TOKEN1","7005246721:AAFPGY9-BsuZR1a6noaRJyQBqrrFwZTEMyI")
    TOKEN2 = getenv("TOKEN2")
    TOKEN3 = getenv("TOKEN3")
    TOKEN4 = getenv("TOKEN4")
    TOKEN5 = getenv("TOKEN5")
    SUDO = getenv("SUDO","6677260209")
else:
    TOKEN1 = ""
    TOKEN2 = ""
    TOKEN3 = ""
    TOKEN4 = ""
    TOKEN5 = ""
    SUDO = []
