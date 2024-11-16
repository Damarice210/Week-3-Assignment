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

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"The final price after applying the discount is: {final_price}")
