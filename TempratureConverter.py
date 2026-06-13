celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
 
print(f"{celsius}°C is equal to {fahrenheit}°F")
 
if celsius <= 0:
    print("It's freezing! Wear heavy winter clothing.")
elif celsius <= 15:
    print("It's cold. A jacket would help.")
elif celsius <= 25:
    print("Pleasant weather. Light clothing is fine.")
elif celsius <= 35:
    print("It's hot. Stay hydrated.")
else:
    print("Extreme heat! Avoid going out if possible.")
 