import requests
import time
import csv
import os
from datetime import datetime
API_URL = "https://api.coingecko.com/api/v3/simple/price"
HISTORY_FILE = "price_history.csv"
tracked_coins = ["bitcoin", "ethereum"]
currency = "usd"
def fetch_prices(coins, curr):
    params = {
        "ids": ",".join(coins),
        "vs_currencies": curr,
        "include_24hr_change": "true"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Couldn't reach the internet or the API is down right now.")
        return None
    except requests.exceptions.Timeout:
        print("The request took too long and timed out. Try again.")
        return None
    except requests.exceptions.HTTPError as err:
        print(f"API returned an error: {err}")
        return None
    except Exception as err:
        print(f"Something went wrong: {err}")
        return None
def print_table(data, curr):
    if not data:
        print("No data to show.")
        return
    name_width = max(len(c) for c in data) + 2
    print("-" * (name_width + 25))
    print(f"{'Coin':<{name_width}}{'Price':<15}{'24h Change'}")
    print("-" * (name_width + 25))
    for coin, values in data.items():
        price = values.get(curr)
        change = values.get(f"{curr}_24h_change")
        if price is None:
            print(f"{coin:<{name_width}}{'N/A':<15}{'N/A'}")
            continue
        price_str = f"{price:,.2f}"
        if change is not None:
            arrow = "up" if change >= 0 else "down"
            change_str = f"{change:+.2f}% ({arrow})"
        else:
            change_str = "N/A"
        print(f"{coin:<{name_width}}{price_str:<15}{change_str}")
    print("-" * (name_width + 25))
def save_to_history(data, curr):
    file_exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price", "24h_change", "currency"])
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin, values in data.items():
            price = values.get(curr, "")
            change = values.get(f"{curr}_24h_change", "")
            writer.writerow([now, coin, price, change, curr])
def view_prices():
    data = fetch_prices(tracked_coins, currency)
    if data:
        print_table(data, currency)
        save_to_history(data, currency)
def add_coin():
    coin = input("Enter the coin id (example: dogecoin, cardano, solana): ").strip().lower()
    if not coin:
        print("You didn't type anything.")
        return
    check = fetch_prices([coin], currency)
    if check and coin in check:
        if coin not in tracked_coins:
            tracked_coins.append(coin)
            print(f"{coin} added to your tracker.")
        else:
            print(f"{coin} is already being tracked.")
    else:
        print(f"Couldn't find a coin called '{coin}'. Make sure you're using the CoinGecko id.")
def remove_coin():
    print("Currently tracking:", ", ".join(tracked_coins))
    coin = input("Which coin do you want to remove? ").strip().lower()
    if coin in tracked_coins:
        if len(tracked_coins) == 1:
            print("You need to keep tracking at least one coin.")
            return
        tracked_coins.remove(coin)
        print(f"{coin} removed.")
    else:
        print("That coin isn't in your list.")
def auto_refresh():
    try:
        seconds = int(input("Refresh every how many seconds? "))
    except ValueError:
        print("That's not a number, going back to the menu.")
        return
    print("Auto refreshing... press Ctrl+C to stop and return to the menu.\n")
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Live prices (updates every {seconds}s) - {datetime.now().strftime('%H:%M:%S')}\n")
            view_prices()
            time.sleep(seconds)
    except KeyboardInterrupt:
        print("\nStopped auto refresh.")
def change_currency():
    global currency
    new_currency = input("Enter currency code (usd, eur, gbp, inr...): ").strip().lower()
    if new_currency:
        currency = new_currency
        print(f"Currency switched to {currency.upper()}")
def show_menu():
    print("\n=== Crypto Price Tracker ===")
    print("1. View Prices")
    print("2. Add Cryptocurrency")
    print("3. Remove Cryptocurrency")
    print("4. Refresh Data (auto)")
    print("5. Change Currency")
    print("6. Exit")
def main():
    print("Welcome to the Crypto Price Tracker!")
    print(f"Currently tracking: {', '.join(tracked_coins)}")
    while True:
        show_menu()
        choice = input("Pick an option (1-6): ").strip()
        if choice == "1":
            view_prices()
        elif choice == "2":
            add_coin()
        elif choice == "3":
            remove_coin()
        elif choice == "4":
            auto_refresh()
        elif choice == "5":
            change_currency()
        elif choice == "6":
            print("See you later!")
            break
        else:
            print("That's not a valid option, try again.")
if __name__ == "__main__":
    main()