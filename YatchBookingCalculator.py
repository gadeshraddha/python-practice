
guests = int(input("Enter number of guests: "))
package = input("Enter package type (basic/premium/luxury): ").strip().lower()

base_price = 0

if package == "basic":
    base_price = 5000
elif package == "premium":
    base_price = 9000
elif package == "luxury":
    base_price = 15000
else:
    print("Invalid package type.")

if base_price > 0:
    if guests > 10:
        extra_guests = guests - 10
        total = base_price + extra_guests * 500
        print(f"Extra charge for {extra_guests} additional guests applied.")
    else:
        total = base_price

    if guests > 20:
        discount = total * 0.10
        total -= discount
        print("10% group discount applied!")

    print(f"Total booking price: ₹{total}")