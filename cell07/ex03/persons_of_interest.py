def famous_births(figures):
    sorted_figures = sorted(figures, key=lambda person: person["date_of_birth"])
    for person in sorted_figures:
        print(f"{person["name"]} ({person["date_of_birth"]})")

if __name__ == "__main__":
    people = [
        {"name": "Albert Einstein", "date_of_birth": "1879-03-14"},
        {"name": "Isaac Newton", "date_of_birth": "1643-01-04"},
        {"name": "Marie Curie", "date_of_birth": "1867-11-07"},
        {"name": "Ada Lovelace", "date_of_birth": "1815-12-10"}
    ]

    famous_births(people)