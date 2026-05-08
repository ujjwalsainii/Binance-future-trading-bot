from binance.client import Client
from config import API_KEY, API_SECRET
from utils.logger import logger

class BinanceService:

    def __init__(self):

        try:
            self.client = Client(
                API_KEY,
                API_SECRET,
                testnet=True
            )

            logger.info("Binance client initialized")

        except Exception as e:
            logger.error(f"Initialization error: {e}")
            print(f"Initialization error: {e}")

    def get_balance(self):

        try:
            balance = self.client.futures_account_balance()
            return balance

        except Exception as e:
            logger.error(f"Balance fetch error: {e}")
            print(f"Balance fetch error: {e}")

    def place_market_order(self, symbol, side, quantity):

        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )

            logger.info(f"Order placed: {order}")

            return order

        except Exception as e:
            logger.error(f"Order placement failed: {e}")
            print(f"Order placement failed: {e}")
            return None