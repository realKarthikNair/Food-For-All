import firebase_admin
from firebase_admin import db
import os

cred_object = firebase_admin.credentials.Certificate(os.path.join("keys","foodforall-45f30-firebase-adminsdk-9xuwc-34706f48e2.json"))

firebase_admin.initialize_app(cred_object, {
         'databaseURL': 'https://foodforall-45f30-default-rtdb.firebaseio.com'
})

class Backend:
    def __init__(self):
        self.ref = db.reference('DB')

    # restaurant is the child node

    # def add_restaurant(self, rest_id, rest_name, foods, org_type):
    #     self.org_type_ref = self.ref.child(org_type)
    #     # create foods node
    #     self.foods_ref = self.org_type_ref.child(rest_id).child('foods')
    #     self.foods_ref.set(foods)

    def validate_user(self, id, password, org_type):
        self.users_ref = self.ref.child(org_type)
        return self.users_ref.child(id).get()['password'] == password

    def check_user(self, id, org_type):
        self.users_ref = self.ref.child(org_type)
        return self.users_ref.child(id).get() != None

    
    def add_user(self, id, name, password, org_type):
        self.users_ref = self.ref.child(org_type)
        self.users_ref.child(id).set({
            'name': name,
            'password': password
        })

    # add multiple foods with their quantities
    def add_foods(self, rest_id, foods, org_type):
        self.foods_ref = self.ref.child(org_type).child(rest_id).child('foods')
        self.foods_ref.set(foods)

# login else signup


def login(org_type):
    id = input("Enter your id: ")
    backend = Backend()
    if backend.check_user(id):
        password = input("Enter your password: ")
        if backend.validate_user(id, password):
            print("Login successful")
        else:
            print("Invalid password")
    else:  
        print("User not found. Please signup!")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        backend.add_user(id, name, password, org_type)
        print("User added successfully")

food_n=int(input("Enter the number of food items you want to add: "))
foods={}
for i in range(food_n):
    food=input("Enter the food item: ")
    quantity=int(input("Enter the quantity: "))
    foods[food]=quantity


print(backend.add_foods(id, foods))



# foods = {
#     food1: quantity1,
#     food2: quantity2
# }

# backend = Backend()
# backend.add_restaurant(rest_name, rest_id, foods)

