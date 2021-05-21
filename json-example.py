# Dear Students, this is a quick review of JSON (JavaScript) or Dictionary (Python)
cars_info = [
    {
        "brand": "Honda",
        "model": "2019",
        "color": "white"
    },
    {
        "brand": "Fiat",
        "model": 2010,
        "color": "blue"
    },
    {
        "brand": "Volvo",
        "model": 2012,
        "color": "red"
    }
]

print(cars_info)
print("**********************")

for item in cars_info:
    print(item)

print("**********************")
count = 1
for car in cars_info:
    print(f"Car#{count}: ")
    print(car["brand"])
    print(car["model"])
    print(car["color"])
    print("************")
    count += 1
