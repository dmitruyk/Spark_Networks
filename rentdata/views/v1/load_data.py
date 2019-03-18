from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
import json


def load_data(request):
    if request.method == 'GET':
        with open('rentdata/1.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
            return JsonResponse(data, status=400)
    else:
        return JsonResponse({'POST': 'load_data'}, status=400)


def index(request):
    if request.method == 'GET':
        return JsonResponse({'GET': 'Not existed'}, status=400)
    else:
        return JsonResponse({'POST': 'Not existed'}, status=400)

