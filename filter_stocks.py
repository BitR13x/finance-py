import requests
import pandas as pd
from envi import API_KEY

def calculate_debt_ratio(total_current_assets:int, total_current_liabilities:int) -> float:
    debt_ratio = total_current_assets / total_current_liabilities
    return debt_ratio

def calculate_operating_margin(total_revenue:int, operating_income:int) -> float:
    operating_margin = (total_revenue / operating_income) * 100
    return operating_margin


# ? GET STOCKS IN SECTOR
def get_stocks():
    # Replace 'YOUR_API_KEY' with your Alpha Vantage API key

    # Define the sector you're interested in (e.g., technology)
    sector = 'technology'

    # Get a list of stock symbols in the specified sector
    symbol_url = f'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={API_KEY}&datatype=csv'
    symbol_response = requests.get(symbol_url)

    print(symbol_response.text)
"""     # Filter companies in the specified sector
    tech_companies = symbol_data[symbol_data['SECTOR'] == sector]

    # Fetch balance sheet data for each company in the sector
    balance_sheets = []
    for symbol in tech_companies['SYMBOL']:
        balance_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}&datatype=csv'
        balance_response = requests.get(balance_url)
        balance_data = pd.read_csv(balance_response.url)
        balance_sheets.append(balance_data)

    print(balance_sheets[0])
    return symbol_response
 """



def trading_scan():
    url = "https://scanner.tradingview.com/america/scan"
    request_data = """{"columns":["name","description","logoid","update_mode","type","typespecs","cash_f_operating_activities_ttm","fundamental_currency_code","cash_f_investing_activities_ttm","cash_f_financing_activities_ttm","free_cash_flow_ttm","capital_expenditures_ttm"],"filter":[{"left":"name","operation":"nempty"},{"left":"typespecs","operation":"has_none_of","right":"preferred"},{"left":"sector","operation":"equal","right":"Technology Services"},{"left":"exchange","operation":"in_range","right":["AMEX","NASDAQ","NYSE"]}],"ignore_unknown_fields":false,"options":{"lang":"en"},"range":[0,200],"sort":{"sortBy":"free_cash_flow_ttm","sortOrder":"desc"},"markets":["america"]}"""
    req = requests.post(url, data=request_data )
    return req.text

print(trading_scan())

# TODO: filter by operating margin and debt ratio

# TODO: analyse
