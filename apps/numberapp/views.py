from django.http import JsonResponse
from django.shortcuts import render
from forms import NumberForm
from utils import change


def number_change(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            your_number = form.cleaned_data['your_number']
            number_in_words = change(your_number)
            response = JsonResponse({'normal_number': your_number, 'number_in_words': number_in_words})
            return response
    else:
        form = NumberForm(request.POST)
    return render(request, 'numberapp/base.html', {'form': form})
