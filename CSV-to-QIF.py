'''**************************************************************************/
#
#    @file    CSV_to_QIF.py
#    @author   Mario Avenoso (M-tech Creations)
#    @license  MIT (see license.txt)
#
#    Program to convert from a CSV to a QIF file using a definitions
#    to describe how the CSV is formatted
#
#    @section  HISTORY
#    v0.2 - Added payee ignore option  1/18/2016 feature update
#    v0.1 - First release 1/1/2016 beta release
#
'''#**************************************************************************/


import os, sys, csv, locale
from datetime import datetime
from convert import convertToTransaction
from Settings import Settings
import traceback

#
#     @brief  Takes given CSV and parses it to be exported to a QIF
#
#     @params[in] inf_
#     File that the converted data will go
#     @params[in] settings_
#     settings for converting CSV
#
#
def readCsv(inf_, settings_):
    csvIn = csv.reader(inf_, delimiter=settings_.delimiter)  #create csv object using the given separator

    header_ = settings_.header
    while header_ >= 1: #If there is a header skip the fist line
        next(csvIn, None)  #skip header
        header_ -= 1

    for i, row in enumerate(csvIn):
        try:
            date = datetime.strptime(row[settings_.date], settings_.dateformat)
            amount = locale.atof(row[settings_.amount]) if row[settings_.amount] else None

            if amount != None:
                transaction = convertToTransaction(date, amount, row[settings_.memo], row[settings_.payee])
                if transaction != None:
                    writeFile(transaction)
        except Exception:
            print(f"Error in row {i}: '{row}'", file=sys.stderr)
            raise


#
#     @brief Receives data to be written to and its location
#
#     @params[in] date_
#     Data of transaction
#     @params[in] amount_
#     Amount of money for transaction
#     @params[in] memo_
#     Description of transaction
#     @params[in] payee_
#     Transaction paid to
#
#
# https://en.wikipedia.org/wiki/Quicken_Interchange_Format
#
def writeFile(transaction_):
    print("!Type:Cash")     # Header of transaction, Currently all set to cash

    print("D" + datetime.strftime(transaction_.date, "%d.%m.%Y"))

    print("T" + str(transaction_.amount))

    if transaction_.memo:
        print("M" + str(transaction_.memo))

    if transaction_.payee:
        print("P" + transaction_.payee)

    if transaction_.category:
        print("L" + transaction_.category)

    print("^")  #The last line of each transaction starts with a Caret to mark the end



def writeHeader(settings_):
    if settings_.accountName:
        print("!Account")
        print("N" + settings_.accountName)
        print("TBank")
        print("^")


def convert():
    if len(sys.argv) != 3:  #Check to make sure all the parameters are there
         print('''Input error! Format [import.csv] [import.def]
[import.csv] = File to be converted
[import.def] = Definition file describing csv file''', file=sys.stderr)
         exit(1)

    if not os.path.isfile(sys.argv[2]):
         print('\nInput error! import.def: ' + sys.argv[2] + ' does not exist/cannot be opened!\n', file=sys.stderr)
         exit(2)

    settings = Settings(sys.argv[2])
    
    if not os.path.isfile(sys.argv[1]):
         print('\nInput error! import.csv: ' + sys.argv[1] + ' does not exist/cannot be opened!\n', file=sys.stderr)
         exit(3)

    locale.setlocale(locale.LC_NUMERIC, settings.locale)

    writeHeader(settings)

    with open(sys.argv[1], 'r', encoding=settings.encoding) as fromfile:
        readCsv(fromfile, settings)


if __name__ == '__main__':
    convert() #Start
