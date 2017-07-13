# npv
This is a calculator that can be used to get the net present value of future investments. It uses a simple equation of NPV=PV*(1+rate)^time. It is typically used in the finance world to estimate the future value of an investment based off of the current return.
## Installation
`pip3 install babel` or `pip install babel`
## Usage
```
from babel.numbers import format_currency

pv=int(input('What is Your Present Value:'))

r=float(input('What is Your Interst Rate (As Decimal):'))

t=int(input('What is your Number of Periods (1-99):'))

if t<=99:

    npv=(pv*(1+r)**t)
    
    nnpv=(format_currency(npv,'USD',locale='en_US'))
    
    print('In',t,'year(s), your net present value will be',nnpv)
```
