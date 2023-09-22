# Define a function to calculate Earnings Per Share (EPS)
def calculate_eps(net_income: int, number_of_shares: int) -> int: # number of shares, what share holders hold
    """
    Analyze a company's profitability by examining its EPS over time.
    
    *Use*: 
      Investors use EPS to assess a company's earnings performance over time 
      and compare it to other companies in the same industry.
      It's also a key component in calculating the P/E ratio.
    """
    eps = net_income / number_of_shares
    return eps

# Define a function to calculate Price-to-Earnings (P/E) Ratio
def calculate_pe_ratio(current_price: int, eps: int) -> int:
    """
    Compare the stock's current price to its earnings per share to evaluate its relative value.
    
    *Use*: 
      This ratio helps investors determine if a stock is overvalued 
      or undervalued relative to its earnings potential.
      A higher P/E ratio may indicate higher growth expectations, 
      but it can also suggest an overvaluation.

    lower better
    """
    pe_ratio = current_price / eps
    return pe_ratio

# Define a function to calculate Price-to-Book (P/B) Ratio
def calculate_pb_ratio(current_price: int, book_value_per_share: int) -> int:
    """
    Compare the stock's market price to its book value, indicating if the stock is overvalued or undervalued.
    
    *Use*: 
      This ratio is used to determine if a stock is undervalued 
      or overvalued based on its accounting value. 
      It's commonly used in evaluating financial and banking stocks.
    
    lower better
    """
    pb_ratio = current_price / book_value_per_share
    return pb_ratio

# Define a function to calculate Debt-to-Equity Ratio
def calculate_de_ratio(total_debt: int, total_equity: int) -> int:
    """
    Evaluate the company's financial leverage and its ability to manage debt.
    
    *Use*: 
      Investors and analysts use this ratio to 
      assess a company's financial risk. 
      A higher D/E ratio can suggest higher financial 
      risk and potential difficulties in servicing debt.
    """
    de_ratio = total_debt / total_equity
    return de_ratio

# Define a function to calculate Dividend Yield
def calculate_dividend_yield(dividend_amount: int, dividends_per_year: int, current_price: int) -> int:
    """
    For dividend-paying stocks, analyze the yield as a percentage of the stock price.
    
    *Use*: 
      Income-focused investors use this ratio to identify stocks
      that provide a steady income stream. 
      It's also used for comparing dividend-paying stocks to alternative investments.
    """
    dividend_yield = ((dividend_amount * dividends_per_year) / current_price) * 100
    return dividend_yield

# Growth Prospects