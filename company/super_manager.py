from company.manager import Manager

class SuperManager(Manager):
    def __init__(self, name, wage, managedUnit):
        # Sistemo il costruttore con super() per la parte del Manger
        super().__init__(name, wage, managedUnit)