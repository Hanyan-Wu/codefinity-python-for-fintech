def calculate_financial_ratios(companies):
    ratios = {}
    for company in companies:
        name = company.get("name", "Unknown")
        company_ratios = {}

        price = company.get("price")
        earnings = company.get("earnings")
        net_income = company.get("net_income")
        equity = company.get("equity")
        debt = company.get("debt")

        # Write your code here
        try:
            pe_ratio = price / earnings 
            
        except (TypeError, ZeroDivisionError):
            pe_ratio = None 
        company_ratios['P/E'] = pe_ratio

        try:
            roe_ratio = net_income / equity

        except (TypeError, ZeroDivisionError):
            roe_ratio = None 
        company_ratios['ROE'] = roe_ratio
        
        try:
            doe_ratio = debt / equity

        except (TypeError, ZeroDivisionError):
            doe_ratio = None 
        company_ratios['Debt-to-Equity'] = doe_ratio
        
        ratios[name] = company_ratios
    return ratios

companies = [
    {
        "name": "AlphaCorp",
        "price": 100,
        "earnings": 5,
        "net_income": 20,
        "equity": 100,
        "debt": 50
    },
    {
        "name": "BetaInc",
        "price": 80,
        "earnings": 0,
        "net_income": 15,
        "equity": 0,
        "debt": 30
    },
    {
        "name": "GammaLLC",
        "price": 60,
        "earnings": 4,
        "net_income": None,
        "equity": 80,
        "debt": None
    }
]

result = calculate_financial_ratios(companies)
print(result)
