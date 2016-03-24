# balance, monthlyPaymentRate are any variable

paidPayment = 0
for month in range(1,13):
    minPayment = balance * monthlyPaymentRate
    balance = balance - minPayment
    interest = (annualInterestRate/12.0) * balance
    balance = balance + interest
    paidPayment = paidPayment + minPayment
    print "month: " + str(month)
    print "Minimum monthly payment: " + str(round(minPayment,2))
    print "Remaining balance: " + str(round(balance,2))
print "Total paid: " + str(round(paidPayment,2))
print "Remaining balance: " + str(round(balance,2))
