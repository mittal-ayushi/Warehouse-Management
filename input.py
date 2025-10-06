import json

filename = "input.json"
with open(filename, "r") as f:
    data = json.load(f)

item = {}
item["Item ID"] = input("Enter Item ID: ")
item["Name"] = input("Enter Name: ")
item["Width"] = int(input("Enter Width: "))
item["Length"] = int(input("Enter Length: "))
item["Height"] = int(input("Enter Height: "))
item["Weight"] = int(input("Enter Weight: "))
item["Priority"] = int(input("Enter Priority: "))
item["Expiry"] = input("Enter Expiry Date (YYYY-MM-DD): ")
item["Usage Limit"] = input("Enter Usage Limit: ")
item["Preferred Zone"] = input("Enter Preferred Zone: ")

# append new item
data.append(item)

# write back to file
with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print("Item added successfully to input.json!")


