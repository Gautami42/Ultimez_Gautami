pizza = {
    "Large": 8,
    "Medium": 6,
    "Regular": 4,
    "Small": 1
}
individuals = int(input("Enter the number of people: "))


large = individuals // pizza["Large"]
medium = (individuals % pizza["Large"]) // pizza["Medium"]
regular = (individuals % pizza["Medium"]) // pizza["Regular"]
small = (individuals % pizza["Regular"]) // pizza["Small"]


print(f"\nNumber of individuals: {individuals}")
print(f"Large Pizzas: {large}")
print(f"Medium Pizzas: {medium}")
print(f"Regular Pizzas: {regular}")
print(f"Small Pizzas: {small}")


total_slices = (large * pizza["Large"]) + (medium * pizza["Medium"]) + (regular * pizza["Regular"]) + (small * pizza["Small"])

