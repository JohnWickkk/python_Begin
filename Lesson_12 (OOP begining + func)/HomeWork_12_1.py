net_cost_price_data = {'Toshiba': 500, 'Apple': 1000}
upgrade_cond_disc = {'Toshiba': 25, 'Apple': 75}
avg_price = {'Toshiba': 1200, 'Apple': 3000}


class Product:
    def __init__(self, name, net_cost_price, avg_price, upgrade_cond_disc):
        self.name = name
        self.net_cost_price = net_cost_price
        self.avg_price = avg_price
        self.upgrade_cond_disc = upgrade_cond_disc

    def calculate_investment_return(self):
        trade_revenue = self.avg_price - self.net_cost_price
        discount_factor = 1 - (100 - self.upgrade_cond_disc) / 100
        return trade_revenue * discount_factor


brand_name = input("Enter brand name (Toshiba or Apple)")


investment_return = Product(brand_name, net_cost_price_data[brand_name], avg_price[brand_name],
                            upgrade_cond_disc[brand_name]).calculate_investment_return()
print(f"Investment return for {brand_name}: {investment_return}")
