german_city_names = {
    "Munich": "München",
    "Munchen": "München",
    "Cologne": "Köln",
    "Frankfurt": "Frankfurt am Main",
    "Frankfurt on the Main": "Frankfurt am Main",
    "Cologne": "Köln",
    "Dusseldorf": "Düsseldorf"
}


async def convert_to_german_chars(word):
    for english, german in german_city_names.items():
        word = word.replace(english, german)
    return word

