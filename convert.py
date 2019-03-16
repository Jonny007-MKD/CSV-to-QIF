from Transaction import Transaction

def convertToTransaction(date, amount, memo, payee):
    t = Transaction()
    t.date = date
    t.amount = amount
    t.memo = memo
    t.payee = getPayee(date, amount, memo, payee)
    t.category = getCategory(date, amount, memo, payee)
    return t

def getPayee(date, amount, memo, payee):
    return payee

def getCategory(date, amount, memo, payee):
    return None
