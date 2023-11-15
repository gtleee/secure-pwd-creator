import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .utils import PasswordGenerator


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    length = 12
    password = PasswordGenerator(length=length).generate()

    context = {'password': password, 'length': length}
    return render(request, 'home.html', context)


@csrf_exempt
@require_http_methods(['POST'])
def generate_password(request):
    try:
        data = json.loads(request.body)
        length = int(data.get('length', 12))
        uppercase = data.get('uppercase', False)
        lowercase = data.get('lowercase', False)
        numbers = data.get('numbers', False)
        symbols = data.get('symbols', False)

        generator = PasswordGenerator(length, uppercase, lowercase, numbers, symbols)
        password = generator.generate()
        return JsonResponse({'password': password})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
