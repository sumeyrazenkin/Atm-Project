import json
file = "customers.json"
def add_customer():
    customers = {}
    with open (file, "r") as f:
        pyfile = json.load(f)
    customers["Customer_ID"] = int(input("Customer ID:"))
    customers["Name"] = input("Customer Name:")
    customers["Email"] = input("Customer Email:")
    customers["Password"] = input("Customer Password:")
    customers["Current Balance"] = float(input("Customer Current Balance:"))
    pyfile.append(customers)
    
    with open (file, "w") as f:
        json.dump(pyfile, f, indent=2)    

add_customer()