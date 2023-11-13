
from django.shortcuts import render
from django.http import HttpResponse
from .models import*

'''
def index(request):
    return HttpResponse("소금의 투두 리스트 만들기")
'''


def index(request):
    return render(request, "my_to_do_app/index.html")

def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo= Todo(content =user_input_str)
    new_todo.save()

    return HttpResponse("메모한 건 여기에 쌓여요 : " + user_input_str)





