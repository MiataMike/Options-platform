import math
def put(stock_price, strike_price,risk_free, percent_year, volatility):
    call_price = call(stock_price, strike_price,risk_free, percent_year, volatility)
    P =  c2pParity(call_price, stock_price, strike_price, risk_free, percent_year)
    return P

def call(stock_price, strike_price,risk_free, percent_year, volatility):
    S = stock_price
    K = strike_price
    r = risk_free
    t = percent_year
    sigma = volatility
    d1num = math.log(S/K) + (r + sigma**2 / 2) * t
    d2num = math.log(S/K) + (r - sigma**2 / 2) * t
    dden = sigma * math.sqrt(t)
    get = S * phi(d1num/dden)
    pay = K * math.exp(-r*t) * phi(d2num/dden)
    return get - pay

def day2yr(days):
   return days/365

def p2cParity(put_price, stock_price, strike_price, risk_free, percent_year):
    P = put_price
    S0 = stock_price
    X = strike_price
    r = risk_free
    t = percent_year
#C + Xe^rt = P + S0
    C = P + S0 - (X * math.exp(-r*t))
    return C

def c2pParity(call_price, stock_price, strike_price, risk_free, percent_year):
    C = call_price
    S0 = stock_price
    X = strike_price
    r = risk_free
    t = percent_year
#C + Xe^rt = P + S0
    P = C + (X * math.exp(-r*t)) - S0
    return P

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
