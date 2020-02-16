import json

class Settings:
    def __init__(self, defpath):
        with open(defpath,'r') as deffile:
            deff = json.load(deffile)
            self.dateformat  = deff["meta"]["dateformat"]
            self.delimiter   = deff["meta"]["delimiter"]
            self.encoding    = deff["meta"]["encoding"]
            self.locale      = deff["meta"]["locale"]
            self.header      = int(deff["meta"]["header"])
            self.date        = int(deff["columns"]["date"])
            self.amount      = int(deff["columns"]["amount"])
            self.memo        = int(deff["columns"]["memo"])
            self.payee       = int(deff["columns"]["payee"])
