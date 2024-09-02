
#Products

def individual_serial(product) -> dict:
    
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "quantity": product["quantity"]
    }


def get_all(products):
    return [individual_serial(product) for product in products]
    
    

#Users

def individual_user(user) -> dict:
    
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


def get_users(users):
    return[individual_user(user) for user in users]