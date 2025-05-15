temperature = float(input("Enter the current temperature in Celsius: "))

if temperature >= 25:
    print("It's warm. You can wear light and soft clothes.")
elif 18 <= temperature < 25:
    print("It's a bit cool. Wear light clothes but keep a light jacket handy.")
else:
    print("It's cold. Better to wear a pullover or jacket to avoid getting sick.")