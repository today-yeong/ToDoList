
from django.shortcuts import render
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("소금의 투두 리스트 만들기")
'''


def index(request):
    return render(request, "my_to_do_app/index.html")

