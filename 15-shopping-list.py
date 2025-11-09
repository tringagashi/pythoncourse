shopping = []

print("Type 'stop' to finish.")

while True:
    item = input("Add item: ")
    if item.lower() == "stop":
        break
    shopping.append(item)

print("\nYour shopping list:")
for item in shopping:
    print("-", item)
