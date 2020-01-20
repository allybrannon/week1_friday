for country in digitalcrafts:
    print(country)
    for state in digitalcrafts[country]:
    print(country, state, end=': ')
        print(state)
    for city in digitalcrafts[country][state]:
        print(city)