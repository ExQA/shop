from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Author


# Create your views here.


def index(request):
    ctx = {}
    ctx['a'] = 45
    ctx['some_value'] = 'value'
    all_books = Book.objects.all()  # 'SELECT * FROM app1_book;'
    ctx['all_books'] = all_books
    ctx['current_tab'] = 'home'
    # for book in all_books:
    #     print(book.title)
    # print(all_books)
    return render(request, 'pages/home.html', ctx)


from .calc import calc_obj


def calc(request):
    ctx = {}
    ctx['operations'] = calc_obj.keys()
    ctx['current_tab'] = 'calc'
    if request.method == 'GET':
        print('GET!')
    elif request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num'))
            operation = request.POST.get('operation')
            second_num = float(request.POST.get('second_num'))
            secret = request.POST.get('secret_code')
            print(secret)
            result = calc_obj[operation](first_num, second_num)
            print(result)
            ctx['result'] = result
        except (Exception,) as e:
            ctx['msg'] = e
        # print('POST!!!!!', type(first_num), operation, second_num)

    return render(request, 'pages/calculator.html', ctx)


def examples(request):
    ctx = {}
    ctx['current_tab'] = 'examples'
    ctx['bool_value'] = False
    ctx['some_value'] = 150
    ctx['some_list'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render(request, 'pages/examples.html', ctx)


def book_info(request, id):
    # print(id)
    ctx = {}
    try:

        book = Book.objects.get(pk=id)
        print(book.books_read_with.all())
        current_author = Author.objects.get(id=book.author.id)
        ctx['book'] = book
        ctx['book_author'] = Book.objects.filter(author=current_author).exclude(pk__in=[book.id])
        return render(request, 'pages/book_info.html', ctx)
    except Exception as e:
        print(e)
        return redirect('/')


def all_books_for_author(request, id_author):
    try:
        ctx = {}
        author_target = Author.objects.get(id=id_author)
        ctx['all_books'] = Book.objects.filter(author=author_target)
        ctx['current_author'] = author_target
        return render(request, 'pages/home.html', ctx)
    except Exception as e:
        return redirect('/')
    print(all_book)
    return HttpResponse('author id ' + str(author_target))
