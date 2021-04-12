from benaxfrwork.templates import render


def main_view(request):
    check = request.get('check', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', check=check)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"
