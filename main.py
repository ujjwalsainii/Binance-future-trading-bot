from services.binance_client import BinanceService
from validators import validate_side, validate_order_type

def main():

    bot = BinanceService()

    print("===== Binance Futures Testnet Bot =====")

    symbol = input("Enter symbol: ").upper()

    side = input("Enter side (BUY/SELL): ").upper()

    if not validate_side(side):
        print("Invalid side")
        return

    order_type = input("Enter order type (MARKET/LIMIT): ").upper()

    if not validate_order_type(order_type):
        print("Invalid order type")
        return

    quantity = float(input("Enter quantity: "))

    price = None

    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))

    print("\nFetching balance...\n")

    balance = bot.get_balance()

    print(balance)

    print("\nPlacing order...\n")

    order = bot.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print("\nOrder Response:\n")

    print(order)

if __name__ == "__main__":
    main()