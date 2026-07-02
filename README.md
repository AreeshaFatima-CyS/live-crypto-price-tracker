Live Cryptocurrency Price Tracker

A simple Python CLI application that fetches and displays live cryptocurrency prices using the CoinGecko API. Track multiple coins, auto-refresh prices, switch currencies, and log price history to a CSV file.

Features


Live price fetching using the CoinGecko public API
Track multiple cryptocurrencies at once
24-hour price change shown alongside current price
Auto-refresh mode with a custom interval
Add or remove coins from your watchlist anytime
Switch between currencies (USD, EUR, GBP, INR, etc.)
Price history automatically saved to price_history.csv
Handles API errors, timeouts, and invalid coin names gracefully


Requirements


Python 3.7 or higher
requests library


Installation


Clone this repository


git clone https://github.com/your-username/live-crypto-price-tracker.git
cd live-crypto-price-tracker


Install the required library


pip install requests

Usage

Run the script:

python crypto_tracker.py

You'll see a menu like this:

=== Crypto Price Tracker ===
1. View Prices
2. Add Cryptocurrency
3. Remove Cryptocurrency
4. Refresh Data (auto)
5. Change Currency
6. Exit

Menu Options

OptionWhat it does1Shows current prices and 24h change for tracked coins2Add a new coin to track (requires the CoinGecko coin id)3Remove a coin from your watchlist4Auto-refresh prices at a chosen interval (Ctrl+C to stop)5Change the display currency (usd, eur, gbp, inr, etc.)6Exit the application

Finding a Coin ID

When adding a coin, use its CoinGecko ID, not its ticker symbol.

CoinTickerCoin IDBitcoinBTCbitcoinEthereumETHethereumDogecoinDOGEdogecoinSolanaSOLsolanaCardanoADAcardanoRippleXRPripple

To find any coin's ID, search for it on coingecko.com and check the last part of the URL, e.g. coingecko.com/en/coins/solana → id is solana.

Price History

Every time you view prices, they're appended to price_history.csv in the same folder, with columns:

timestamp, coin, price, 24h_change, currency

Default Tracked Coins

By default, the app tracks bitcoin and ethereum. You can add or remove coins from the menu once the app is running.

Project Structure

live-crypto-price-tracker/
├── crypto_tracker.py
├── price_history.csv   (created automatically after first run)
└── README.md

Notes


Requires an active internet connection since prices are fetched live.
Uses the free tier of the CoinGecko API, so no API key is needed.


for demo video cick here
https://drive.google.com/file/d/1L6fTu68KsPAMbyuaS5xwccIbPxebuv_k/view?usp=drive_link




