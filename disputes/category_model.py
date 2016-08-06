from django.db import models

import json


class DisputeCategory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class DisputeCategoryQuestion(models.Model):
    dispute_category = models.ForeignKey(
        'DisputeCategory',
        on_delete=models.CASCADE
    )

    question = models.TextField()


def load_categories():
    with open('disputes/category_questions.json') as data_file:
        data = json.load(data_file)

    for category_data in data:
        category, _ = DisputeCategory.objects.get_or_create(
            category=category_data['category']
        )
        for question_data in category_data['questions']:
            question, _ = DisputeCategoryQuestion.objects.get_or_create(
                question=question_data['question']
            )
