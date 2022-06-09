from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def news(request):
    m_news = News.objects.all()
    return render(request, 'main/news.html', {'title': 'Новости', 'm_news': m_news})


def index(request):
    return render(request, 'main/index.html')


def registration(request):
    return render(request, 'main/registration.html')


def about(request):
    return render(request, 'main/about.html')


def video(request):
    return render(request, 'main/video.html')


def school(request):
    return render(request, 'main/school.html')


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            # response = HttpResponse()
            # response.status_code = 200
            # print('good')
            # return response
            return redirect('news')
        else:
            error = 'Форма была неверной'
    form = NewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_news.html', context)
