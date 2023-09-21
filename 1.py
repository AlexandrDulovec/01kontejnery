cars = {
    "Ford Mustang": 2022,
    "Toyota Camry": 2021,
    "Honda Civic": 2020,
    "Chevrolet Corvette": 2022,
    "Volkswagen Golf": 2021
}
x = len(cars)

for model, year in cars.items():
    print(f"Model: {model}, Rok výroby: {year}")


delka_slovniku = len(cars)
print(delka_slovniku)  


cars["Ford Mustang"] = 2012
cars["Toyota Camry"] = 2011

print("\nUpravený obsah slovníku:")
for model, rok in cars.items():
    print(f"Model: {model}, Rok výroby: {rok}")