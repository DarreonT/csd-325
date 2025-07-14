def city_country(city, country, population, language=None):
    if language:
        return f"{city}, {country} - population {population}, {language}"
    else:
        return f"{city}, {country} - population {population}"

# Call the function with just city and country
print(city_country("Nairobi", "Kenya", 4500000))

# Call the function with city, country, and population
print(city_country("Tokyo", "Japan", 14000000))

# Call the function with all four arguments: city, country, population, language
print(city_country("Santiago", "Chile", 5000000, "Spanish"))

