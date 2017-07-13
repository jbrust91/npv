from babel.numbers import format_currency
#PV equals present value
pv=int(input('What is Your Present Value:'))
#r equals your yearly interest rate
r=float(input('What is Your Interst Rate (As Decimal):'))
#t equals your number of periods
t=int(input('What is your Number of Periods (1-99):'))
if t<=99:
    npv=(pv*(1+r)**t)
    nnpv=(format_currency(npv,'USD',locale='en_US'))
    print('In',t,'year(s), you will have',nnpv)
while t>99:
    print('Please try a different number')
    t=int(input('What is your Number of Periods (1-99):'))
    if t<=99:
        npv=(pv*(1+r)**t)
        nnpv=(format_currency(npv,'USD',locale='en_US'))
        print('In',t,'year(s), your net present value will be',nnpv)
        break
    if t>99:
        continue

