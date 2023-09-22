import yfinance as yf
from fundamental import (
    calculate_eps, calculate_de_ratio,
    calculate_dividend_yield, calculate_pb_ratio,
    calculate_pe_ratio
)
#? https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{stock_symbol}?period=quarter


def fundamental_analysis(stock: yf.Ticker) -> (float, float, float, float, float, float):
    # Quarterly
    financials = stock.quarterly_income_stmt
    balance_sheet = stock.quarterly_balance_sheet
    cash_flow = stock.quarterly_cash_flow
    statistic = stock.info

    # Get specific financial metrics from the income statement
    total_revenue = financials.loc['Total Revenue'].iloc[0]
    operating_income = financials.loc['Operating Income'].iloc[0]

    # Get specific financial metrics from the balance sheet
    total_current_assets = balance_sheet.loc['Current Assets'].iloc[0]
    total_current_liabilities = balance_sheet.loc['Current Liabilities'].iloc[0]

    # Get specific cash flow metrics
    free_cash_flow = cash_flow.loc["Free Cash Flow"].iloc[0]

    # Check if the company is paying dividends
    dividend_info = stock.dividends
    is_paying_dividend = not dividend_info.empty

    # Print the obtained metrics
    print(f"Total Current Assets: {total_current_assets}")
    print(f"Total Current Liabilities: {total_current_liabilities}")
    print(f"Total Revenue: {total_revenue}")
    print(f"Operating Income: {operating_income}")
    print(f"Free Cash Flow: {free_cash_flow}")
    print(f"Paying Dividend: {is_paying_dividend}\n")
    print("--------------------")
    debt_ratio = total_current_assets / total_current_liabilities
    operating_margin = (operating_income / total_revenue ) * 100
    print(f"Able to pay debt: {debt_ratio}")
    print(f"Operating Margin (%): {operating_margin}%")

    if is_paying_dividend:
        sustainable_dividents = is_paying_dividend and free_cash_flow > 0
        print(f"Sustainable dividents: {sustainable_dividents}")
        print(f"Divident yield: {statistic['dividendYield']}")

    an_financials = stock.income_stmt
    an_balance_sheet = stock.balance_sheet
    
    an_free_cash_flow = stock.cashflow.loc["Free Cash Flow"].iloc[0]
    print(f"\nFree Cash Flow: {an_free_cash_flow}")

    eps = calculate_eps(an_financials.loc['Net Income'].iloc[0], statistic['sharesOutstanding'])
    pe_ratio = calculate_pe_ratio(statistic["regularMarketPreviousClose"], eps)
    pb_ratio = calculate_pb_ratio(statistic["regularMarketPreviousClose"], statistic['totalCashPerShare'])
    de_ratio = calculate_de_ratio(an_balance_sheet.loc['Total Debt'].iloc[0], an_balance_sheet.loc['Stockholders Equity'].iloc[0])
    #dividend_yield = dividend_yield = calculate_dividend_yield()
    
    print("--------------------")
    print(f"EPS ratio: {eps}")
    print(f"P/E ratio: {pe_ratio}")
    print(f"P/B ratio: {pb_ratio}")
    print(f"D/E ratio: {de_ratio}")

    return debt_ratio, operating_margin, eps, pe_ratio, pb_ratio, de_ratio


stock_symbol = input("Stock symbol: \n>> ")
# Create a Ticker object for the stock
stock = yf.Ticker(stock_symbol)
fundamental_analysis(stock)

