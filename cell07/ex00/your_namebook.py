def array_of_name(name_dict):
    full_name = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_name.apped(full_name)
    return full_name

if __name__ == "__main__":
    example_dict = {
        "john": "doe",
        "jane": "smith",
        "alice": "johnson"
    }

    names = array_of_name(example_dict)
    print(names)