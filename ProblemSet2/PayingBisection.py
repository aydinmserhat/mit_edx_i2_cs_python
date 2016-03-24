monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentlow = balance / 12
monthlyPaymentUp = (balance*(1+monthlyInterestRate)**12) / 12.0
updatebalance = balance

while abs(balance) > 0.01:

    for month in range(1,13):
        fixminPayment = (monthlyPaymentlow + monthlyPaymentUp) / 2.0
        balance = balance - fixminPayment
        interest = (annualInterestRate/12.0) * balance
        balance = balance + interest

    if balance < -0.001:
        monthlyPaymentUp = fixminPayment
        balance = updatebalance

    elif balance > 0.001:
        monthlyPaymentlow = fixminPayment
        balance = updatebalance

    else:
        break

print "Lowest Payment: " + str(round(fixminPayment,2))