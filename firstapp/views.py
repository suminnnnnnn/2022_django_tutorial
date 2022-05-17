from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import CurriculumForm

from .models import Curriculum

def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)
def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')

def show(request):
    curriculum = Curriculum.objects.all()
    return render(
        request, 'firstapp/show.html', 
        {'data' : curriculum}
        )

def insert(request):
    # 1-linux 입력
    Curriculum.objects.create(name='linux')
    # 2-python 입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js 입력
    Curriculum(name='python').save()
    # 4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def index1(request):
    return HttpResponse('<u>Hello</u>')
def index2(request):
    return HttpResponse('<u>Hi</u>')
def main(request):
    return HttpResponse('<u>Main</u>')
def main(request):
    return HttpResponse('Home')

def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)
def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')

def static(request):
    return render(request, 'firstapp/static.html')

def var(request):
    data = {
            'str': 'text', 'num': 10,
            'list': [1, 2, 3],
            'dict': {'a': 'aaa', 'b': 'bbb'}
            }
    return render(
            request, 'firstapp/var.html', data)\

def tag(request):
    persons = [
            { 'num': 1, 'name': 'Park', 'score': 100 },
            { 'num': 2, 'name': 'Choi', 'score': 70 },
            { 'num': 3, 'name': 'Kim', 'score': 80 }
            ]
    animals = ['Cat', 'Dog']
    context = {
            'persons': persons,
            'animals': animals
            }
    return render(
            request, 'firstapp/tag.html', context)

import datetime
def filter(request):
    c = Curriculum.objects.all()

    context = {
            'curriculum' : c,
            'title': 'Simple Python', 'num': 10,
            'price': 39800.5,
            'animals': ['삵', '칡', '타조', '낙타'],
            'covid': datetime.datetime(2020, 1, 8)
            }
    return render(request, 'firstapp/filter.html', context)

def template(request):
    return render(
        request, 'firstapp/template.html', {}
        )


def form_model(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            #commit False 사용 시 Curriculum 모델 클래스로 반환
            c = form.save(commit=False)
            c.save
            return redirect('/first/form/model/')
    else:
        form = CurriculumForm()
    return render(
    request, 'firstapp/form_model.html',
    { 'form': form }
)