# travel-log

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


def add_new_country(c, v, d):
    newdict = {}
    newdict['country'] = c
    newdict['visits'] = v
    newdict['cities'] = d

    travel_log.append(newdict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
