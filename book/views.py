from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book 

# Create your views here.class HomePageView(TemplateView):
class HomePageView(TemplateView):
    template_name = "home.html"

class BookPageView(ListView):
    model = Book
    template_name = "book.html"
    context_object_name = 'Books'

class BookDetailView(DetailView):
    model = Book
    template_name = "book_details.html"