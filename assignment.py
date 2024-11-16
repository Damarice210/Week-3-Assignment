def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after applying the discount or the original price if discount is below 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage:
original_price = 100.0
discount = 25.0
final_price = calculate_discount(original_price, discount)
print(f"The final price is: {final_price}")
