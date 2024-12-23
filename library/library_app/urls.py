from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, borrow_book, reports

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('borrow/', borrow_book, name='borrow_book'),
    path('borrow/<int:pk>/return/', borrow_book, name='return_book'),
    path('reports/', reports, name='reports'),
    path('', include(router.urls)),
]
