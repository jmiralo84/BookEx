from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from decimal import Decimal


from .models import MainMenu
from .forms import BookForm

from .models import Book

from django.http import HttpResponseRedirect


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse


def index(request):
    breadcrumb_list = [
        {'name': 'Home', 'url': None}  # Home is the current page
    ]

    return render(request,
                  'bookMng/index.html',
                  {
                      # 'item_list': MainMenu.objects.all()
                      'breadcrumb_list': breadcrumb_list,
                  })


def postbook(request):
    submitted = False
    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},  # Link back to home
        {'name': 'Post Book', 'url': None}  # Current page
    ]
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      # 'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'breadcrumb_list': breadcrumb_list,
                  })

def displaybooks(request):
    query = request.GET.get('q', '') # Get the search query
    if query:
        books = Book.objects.filter(name__icontains=query)
    else:
        books = Book.objects.all()

    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'Display Books', 'url': None}
    ]
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      # 'item_list': MainMenu.objects.all(),
                      'books': books,
                      'breadcrumb_list': breadcrumb_list,
                  })


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'Display Books', 'url': reverse('displaybooks')},  # Link back to list
        {'name': book.name, 'url': None}  # Current book, use its name
    ]
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      # 'item_list': MainMenu.objects.all(),
                      'book': book,
                      'breadcrumb_list': breadcrumb_list,
                  })

def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request,
                  'bookMng/book_delete.html',
                  {
                      # 'item_list': MainMenu.objects.all(),
                  })

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def mybooks(request):
    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'My Books', 'url': None}
    ]
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      # 'item_list': MainMenu.objects.all(),
                      'books': books,
                      'breadcrumb_list': breadcrumb_list,
                  })

def add_to_cart(request, book_id):
    if request.method != "POST":              
        return redirect("displaybooks")

    book = get_object_or_404(Book, pk=book_id)

    cart = request.session.get("cart", [])
    if book_id not in cart:
        cart.append(book_id)
        request.session["cart"] = cart
        messages.success(request, f"“{book.name}” added to your cart.")
    else:
        messages.info(request, f"“{book.name}” is already in your cart.")

    return redirect("displaybooks")

def my_cart(request):
    cart_ids = request.session.get("cart", [])
    books = Book.objects.filter(id__in=cart_ids)

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  "bookMng/mybooks.html",
                  {
                      # "item_list": MainMenu.objects.all(),
                      "books": books,

                  })

def cart_page(request):
    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'Cart', 'url': None}
    ]
    cart_ids = request.session.get("cart", [])
    books = Book.objects.filter(id__in=cart_ids)

    subtotal = sum(b.price for b in books) if books else Decimal("0.00")

    return render(
        request,
        "bookMng/cart.html",
        {
            # "item_list": MainMenu.objects.all(),
            "books": books,
            "subtotal": subtotal,
            'breadcrumb_list': breadcrumb_list,
        },
    )
def remove_from_cart(request, book_id):
    if request.method == "POST":
        cart = request.session.get("cart", [])
        if book_id in cart:
            cart.remove(book_id)
            request.session["cart"] = cart
    return redirect("cart_page")

def about_us(request):
    breadcrumb_list = [
        {'name': 'Home', 'url': reverse('index')},
        {'name': 'About Us', 'url': None}
    ]
    return render(
        request,
      'bookMng/about_us.html',
      {
          # 'item_list': MainMenu.objects.all(),
          'breadcrumb_list': breadcrumb_list,
      })