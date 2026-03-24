from Temperature import Temperature_celsiusTOfahrenheit
from Temperature import Temperature_fahrenheitTOcelsius   
from Temperature import Temperature_celsiusTOkelvin

def main():
    print("Temperature Converter")
    print("Please select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("Enter your choice (1/2/3): ")
    
    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = Temperature_celsiusTOfahrenheit.celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
            
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = Temperature_fahrenheitTOcelsius.fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
            
        elif choice == '3':
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = Temperature_celsiusTOkelvin.celsius_to_kelvin(celsius)
            print(f"{celsius}°C is equal to {kelvin}K")
            
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()

  