# class-syntax

class Car():
    def __init__(self):
        self


# Instantiate a Car object
car1 = Car()
# Set the name attribute of the Car object
car1.name = "Toyota"
print(car1.name)


class Bike():
    def __init__(self, model, color, fee=10):
        self.model = model
        self.color = color
        self.fee = fee

    def print():
        print("This is a bike")


# Instantiate a Bike object with model and color
bike1 = Bike("R15", "Red", 1000)
print(bike1.fee)

# Call the print() method of the Bike class
Bike.print()


print("--------------------")


class User():
    def __init__(self, name, age, followers=0, following=0):
        self.name = name
        self.age = age
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("John", 20)
user2 = User("Mary", 25)
user3 = User("Mike", 30)

user1.follow(user2)
user3.follow(user2)

print(f"user1 following {user1.following} users & {user1.followers} followers")
print(f"user2 following {user2.following} users & {user2.followers} followers")
print(f"user3 following {user3.following} users & {user3.followers} followers")
