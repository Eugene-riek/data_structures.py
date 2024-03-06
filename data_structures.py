def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent/100)
        final_price = price - discount
        return final_price
    else:
        final_price = price
        return None

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage(0 - 100): "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print (f"Final price after applying {discount_percent:.1f}% discount: ${final_price:.2f} ")
else:
    print (f"No discount applied. Original price: ${original_price:.2f}")