german_city_names = {
    "Berlin": "Berlin",
    "Hamburg": "Hamburg",
    "Munich": "München",
    "Munchen": "München",
    "Cologne": "Köln",
    "Frankfurt": "Frankfurt am Main",
    "Frankfurt on the Main": "Frankfurt am Main",
    "Stuttgart": "Stuttgart",
    "Cologne": "Köln",
    "Dusseldorf": "Düsseldorf",
    "Dortmund": "Dortmund",
    "Essen": "Essen",
    "Bremen": "Bremen",
    "Leipzig": "Leipzig",
    "Dresden": "Dresden",
    "Hanover": "Hannover"
}


async def convert_to_german_chars(word):
    for english, german in german_city_names.items():
        word = word.replace(english, german)
    return word

