
# Weather Temperature Converter

print("Weather Temperature Converter")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)

if celsius >= 35:
    print("Weather Condition: Very Hot")
elif celsius >= 25:
    print("Weather Condition: Warm")
elif celsius >= 15:
    print("Weather Condition: Pleasant")
else:
    print("Weather Condition: Cold")
