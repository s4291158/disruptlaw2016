import json

with open('disputes/category_questions.json') as data_file:
    category_questions = json.load(data_file)

category_choices = []
for category_data in category_questions:
    category_choices.append(
        (int(category_data['id']), category_data['category'])
    )
