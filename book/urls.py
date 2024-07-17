from django.contrib import admin
from django.urls import path
from .views import HomePageView,BookPageView,BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookPageView.as_view(), name='books'),
    path('books/<int:pk>',BookDetailView.as_view(), name= 'book_details')
]