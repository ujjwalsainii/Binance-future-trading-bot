from utils.logger import logger

class BinanceService:

    def __init__(self):

        try:
            logger.info("Mock Binance client initialized")
            print("Mock Binance client initialized")

        except Exception as e:
            logger.error(f"Initialization error: {e}")
            print(f"Initialization error: {e}")

    def get_balance(self):

        try:

            balance = {
                "asset": "USDT",
                "balance": "10000",
                "availableBalance": "10000"
            }

            logger.info(f"Balance fetched: {balance}")

            return balance

        except Exception as e:
            logger.error(f"Balance fetch error: {e}")
            print(f"Balance fetch error: {e}")

    def place_order(self, symbol, side, order_type, quantity, price=None):

        try:

            order = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
                "price": price,
                "status": "SUCCESS",
                "message": f"{order_type} order executed successfully"
            }

            logger.info(f"Order placed: {order}")

            return order

        except Exception as e:
            logger.error(f"Order placement failed: {e}")
            print(f"Order placement failed: {e}")
            return None