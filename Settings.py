import csv

class Settings:
    def __init__(self, defpath):
        with open(defpath,'r') as deffile:
            csvdeff = csv.reader(deffile, delimiter=',')
            next(csvdeff, None) # ignore first line
            for settings in csvdeff:
                self.date       = int(settings[0])  # convert to int
                self.dateformat = settings[1]
                self.amount     = int(settings[2])  # How much was the transaction
                self.memo       = int(settings[3])  # discription of the transaction
                self.payee      = int(settings[4])  # Where the money is going
                self.delimiter  = settings[5]       # How the csv is separated
                self.header     = int(settings[6])  # Set if there is a header to skip
                self.encoding   = settings[7]
                self.locale     = settings[8]
