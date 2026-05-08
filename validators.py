def validate_side(side):

    return side in ["BUY", "SELL"]

def validate_order_type(order_type):

    return order_type in ["MARKET", "LIMIT"]