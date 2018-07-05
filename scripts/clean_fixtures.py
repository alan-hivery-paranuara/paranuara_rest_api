import json

FRUITS = ['orange', 'apple', 'banana', 'strawberry']


def clean_companies(companies):
    cleaned_companies = []
    for company in companies:
        cleaned = {
            "model": "api.company",
            "pk": company['index'] + 1,
            "fields": {
                "name": company['company']
            }
        }
        cleaned_companies.append(cleaned)

    return cleaned_companies


def clean_food_items(people):
    food_set = set()
    for person in people:
        food_set = food_set.union(set(person['favouriteFood']))
    return list(food_set)


def clean_people(people):
    food_list = clean_food_items(people)
    cleaned_people = []
    for person in people:
        cleaned_person = {
            "model": "api.person",
            "pk": person['index'] + 1,
            "fields": {
                # Non existent company in fixtures, default to null
                "company": person['company_id'] + 1 if person['company_id'] != 100 else None,
                "name": person['name'],
                "age": person['age'],
                "eye_color": person['eyeColor'],
                "deceased": person['has_died'],
                "email": person['email'],
                "phone": person['phone'],
                "address": person['address'],
                "favourite_foods": [food_list.index(item) + 1 for item in person['favouriteFood']],
                "friends": [friend['index'] + 1 for friend in person['friends']]
            }
        }
        cleaned_people.append(cleaned_person)

    cleaned_food_items = []

    for index, item in enumerate(food_list):
        cleaned_item = {
            "model": "api.fooditem",
            "pk": index + 1,
            "fields": {
                "name": item,
                "category": get_food_item_category(item)
            }
        }
        cleaned_food_items.append(cleaned_item)

    return cleaned_people, cleaned_food_items


def get_food_item_category(item):
    if item in FRUITS:
        return "fruit"
    else:
        return "vegetable"


def main():
    with open('resources/companies.json', 'r') as f:
        companies = json.load(f)
    with open('resources/people.json', 'r') as f:
        people = json.load(f)

    cleaned_companies = clean_companies(companies)

    cleaned_people, cleaned_foods = clean_people(people)

    with open('fixtures/companies.json', 'w+') as f:
        json.dump(cleaned_companies, f)

    with open('fixtures/people.json', 'w+') as f:
        json.dump(cleaned_people, f)

    with open('fixtures/food_items.json', 'w+') as f:
        json.dump(cleaned_foods, f)


if __name__ == '__main__':
    main()
