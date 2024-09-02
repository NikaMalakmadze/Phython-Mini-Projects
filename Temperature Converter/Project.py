#Temperature Converter

unit = input(f"Enter is this a Celsius or Fahrenheit(C or F): ")            #unit variable
Temperature = float(input(f"Enter the Temperature: "))                      #temperature variable

if unit == "C":

    Temperature = round((Temperature * 9) / 5 + 32, 1)
    print(f"Temperature in Fahrenheit is: " + str(Temperature) + f"°F")     #converting Celsius to Fahrenheit

elif unit == "F":

    Temperature = round((Temperature - 32) * 5 /9 , 1)                      #converting Fahrenheit to Celsius
    print(f"Temperature in Celsius is: " + str(Temperature) + f"°C")

else:
    print( unit + f" is invalid unit of measurement! ")                     #if input data is not unit of measurement
