temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
if (temp < -58) | (temp > 41):
    print("Temperature is invalid")
else:
    wind_speed = eval(input("Enter the wind speed in miles per hour: "))
    if wind_speed < 2:
        print("Wind is invalid")
    else:
        temp_tc = 35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * wind_speed ** 0.16
        print("The wind chill index is", '{0:.5f}'.format(temp_tc))