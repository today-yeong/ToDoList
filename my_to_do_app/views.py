
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import pandas as pd
from datetime import datetime

'''
def index(request):
    return HttpResponse("소금의 투두 리스트 만들기")
'''


def index(request):
    todos = Todo.objects.all()
    print("From DB:", todos)
    content= {'todos': todos }
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo = Todo(content=user_input_str)
    new_todo.save()

    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("메모한 건 여기에 쌓여요 : " + user_input_str)


def deleteTodo(request):
    delete_todo_id= request.GET['todoNum']
    print('삭제한 id', delete_todo_id)
    todo= Todo.objects.get(id= delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

# 수정된 exportToExcel 함수
def exportToExcel(request):
    todos = Todo.objects.all()

    # 데이터 프레임 생성
    data = {'Content': [], 'Created_at': []}
    for todo in todos:
        data['Content'].append(todo.content)
        data['Created_at'].append(todo.created_at.strftime('%Y-%m-%d %H:%M:%S'))

    df = pd.DataFrame(data)

    # 현재 시간을 기준으로 엑셀 파일명 생성
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    excel_filename = f'todo_export_{timestamp}.xlsx'

    # 엑셀 파일로 저장
    df.to_excel(excel_filename, index=False)

    # 파일 다운로드 응답
    with open(excel_filename, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={excel_filename}'
    return response
