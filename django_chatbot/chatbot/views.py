import os

from django.contrib import auth
from openai import OpenAI
from django.shortcuts import render
from django.http import JsonResponse


# open_api_key = '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';
client = OpenAI(
    api_key=os.getenv("API_TOKEN")
)
def ask_openai(message):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html')


def login(request):
    return render(request, 'login.html')

def register(request):

    return render(request, 'register.html')


def logout (request):
    auth.logout(request)
