def greet():
  print("Good Morning")
  print("Good Morning")
  print("Good Morning")
  
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# Params location 
greet_with("Bolivia", "emanuel")   # name = Bolivia, location = Emanuel
# Params by name
greet_with(location = "Bolivia",   # location = Bolivia, name = Emanuel
           name ="emanuel")