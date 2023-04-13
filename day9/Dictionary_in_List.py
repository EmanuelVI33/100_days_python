travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above


# to be added to the travel_log. 👇
def add_new_country(country: str, visits: int, cities_list: []) -> None:
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities_list
    })


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
