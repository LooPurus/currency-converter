from django.shortcuts import render
import requests


def convert(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/usd').json()
    currencies = response.get('rates')

    if request.method =='GET':
        context = {
            'currencies': currencies
        }
        return render(request=request, template_name='convert_app/index.html', context=context)
    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        result = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)
        context = {
            'currencies': currencies,
            'converted_amount': result,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount
        }

        return render(request=request, template_name='convert_app/index.html', context=context)
