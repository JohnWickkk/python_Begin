net_profit_data = {'Toshiba': 3000, 'Apple': 5000}


def get_upgrade():
    return f"You can upgrade your Toshiba product with a 50% discount!"


def get_investment():
    return net_profit_data.get('Toshiba')  # Get Toshiba's net profit


# No need for a class 'Toshiba' in this case

if __name__ == "__main__":

    laptop_brand = input('Enter your laptop brand (for axample, Toshiba): ')

    if laptop_brand == 'Toshiba':
        print(get_upgrade())
        print(f"Investment return for 1 Toshiba share is {get_investment()} uah")
    else:
        print(f"We don't have information about {laptop_brand} upgrades or investments.")
