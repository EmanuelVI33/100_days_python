# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 4},
    "Germany": ["Berlin", "Hamburg"]
}

# Nested dictionary with a list
santa_cruz_travel_diary = {
    "San Carlos": {"municipalities_visited": ["Divino Niño", "Central"], "total_visited": 5},
    "La Guardia": {"total_visited": 2}
}

# Nested list with a dictionary
nested_list = [santa_cruz_travel_diary, travel_log, {"name": "Emanuel Vaca", "age": 20}]

print(nested_list[2]["name"])

