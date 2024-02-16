from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
sys.path.append('../engines')
# from engines.calculus import generate
from backfiles.middle import definer


@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_info = request.POST
        user_input = user_info.get('user_input')

        response = "Chatbot: " + str(definer(str(user_input)))

        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method.'})
