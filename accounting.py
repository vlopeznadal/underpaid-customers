def accounting(text_file): 
    """Determine which customers did not pay the right amount"""
    # opening a file to read and assigning it to a variable
    customer_orders = open(text_file)
    # for a single order in the file of orders
    for order in customer_orders:
        # removes white space from end of order
        order = order.rstrip()
        # splits order up by delimiter
        words = order.split('|')
        # variable set to cost of a single melon
        melon_cost = 1.00 
        # variable set to customer name found at index 1 of list
        customer_name = words[1] # 
        # variable set to amount of melons customer purchased found at index 2 of list
        customer_melons = float(words[2])
        # variable set to amount customer paid found at index 3 of list
        customer_paid = float(words[3])
        # calculate expeted cost customer should have paid
        customer_expected = customer_melons * melon_cost
        # if the amount paid by the customer is not the same as the expected amount
        if customer_expected != customer_paid:
            # print who the customer is, what they paid, what they should have paid
            print(f"{customer_name} paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")
    # close the text file
    customer_orders.close()
# call the function with the text file passed
accounting("customer-orders.txt")