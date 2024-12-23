import time
from .rule import Rule

class EstamosEnCasaRule(Rule):
    def execute_no_estamos(self):
        print("No estamos en casa")

    def execute_estamos(self):
        print("Estamos en casa")


    def when_no_estamos_en_casa(self):
        condition = {"device": "estamos_en_casa", 
                     "property": "value", 
                     "value": "False"}

        action = self.execute_no_estamos

        return condition, action

    def when_estamos_en_casa(self):
        condition = {"device": "estamos_en_casa", 
                     "property": "value", 
                     "value": "True"}

        action = self.execute_estamos

        return condition, action