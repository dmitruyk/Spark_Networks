from django.test import TestCase
import json

# Create your tests here.

with open('1.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh)

print(data)