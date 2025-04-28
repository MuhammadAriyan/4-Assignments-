def main():
    fahrenheit:int = int(input('Farenheit temperature: '))
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    print(f'Result : {degrees_celsius} degrees Celsius')


if __name__ == '__main__':
    main()