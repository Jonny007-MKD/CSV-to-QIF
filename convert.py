from Transaction import Transaction

def convertToTransaction(date, amount, memo, payee):
    t = Transaction()
    t.date = date
    t.amount = amount
    t.memo = memo
    t.payee = getPayee(date, amount, memo, payee)
    if t.payee == None: return None

    t.category = getCategory(date, amount, memo, payee, t.payee)

    return t

def getPayee(date, amount, memo, payee):
    if memo == "Tagessaldo": return None

    for a, b in payeeToPayee.items():
        if a in payee.lower(): return b

    return payee

def getCategory(date, amount, memo, payeeOld, payeeNew):
    if payeeNew in payeeNewToCategory: return payeeNewToCategory[payeeNew]

    if "amazon web" in payeeOld.lower(): return "Sonstige Ausgaben:Backup";
    return None

payeeNewToCategory = {
    "McDonalds": "Lebensmittel:Imbiss",
}

payeeToPayee = {
    "mcdonald": "McDonalds",
    "mc donald": "McDonalds",
}

