from datetime import datetime
import math

# Get user input for tire dimensions
width = float(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 55): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 16): "))

# Calculate the volume of the tire
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000

# Determine the price based on tire size
if width == 205 and aspect_ratio == 55 and diameter == 16:
    price = 75.00  # Example price for 205/55R16
elif width == 215 and aspect_ratio == 60 and diameter == 17:
    price = 85.00  # Example price for 215/60R17
elif width == 225 and aspect_ratio == 50 and diameter == 18:
    price = 95.00  # Example price for 225/50R18
elif width == 235 and aspect_ratio == 65 and diameter == 17:
    price = 105.00  # Example price for 235/65R17
else:
    price = None

# Display the results
print(f"\nThe approximate volume of the tire is: {volume:.2f} liters")
if price:
    print(f"The price for a {width}/{aspect_ratio}R{diameter} tire is: ${price:.2f}")
else:
    print("Sorry, we do not have pricing information for the specified tire size.")

# Ask the user if they want to buy the tires
buy_tires = input("\nWould you like to buy these tires? (yes/no): ").strip().lower()
phone_number = ""

if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ").strip()

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Append data to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, ")
    if price:
        file.write(f"${price:.2f}, ")
    else:
        file.write("Price not available, ")
    
    if buy_tires == "yes":
        file.write(f"{phone_number}\n")
    else:
        file.write("No purchase\n")

print("\nData saved to volumes.txt")






