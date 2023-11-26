class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello~~!!")
        print(f"My name is {self.name}")

        
user_1 = User("Choco", 30)

user_1.hello();
