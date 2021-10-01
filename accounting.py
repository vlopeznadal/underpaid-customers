def accounting(text_file):
    customer_orders = open(text_file)
    for order in customer_orders:
        order = order.rstrip()
        words = order.split('|')

        melon_cost = 1.00
        customer_name = words[1]
        customer_melons = float(words[2])
        customer_paid = float(words[3])
        customer_expected = customer_melons * melon_cost
        if customer_expected != customer_paid:
            print(f"{customer_name} paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")
    customer_orders.close()
accounting("customer-orders.txt")