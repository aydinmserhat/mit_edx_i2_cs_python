# balance, annualInterestRate are any variable

updatebalance = balance
fixminPayment = 10
while True:
    for month in range(1,13):
        balance = balance - fixminPayment
        interest = (annualInterestRate/12.0) * balance
        balance = balance + interest
    if balance > 0:
        balance = updatebalance
        fixminPayment = fixminPayment + 10
        continue
    else:
        break
print "Lowest Payment: " + str(fixminPayment)