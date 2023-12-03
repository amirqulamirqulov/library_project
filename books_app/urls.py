from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BooksListApiView, BooksDetailApiView, BooksDeleteApiView, BooksUpdateApiView, \
    BooksListCreateApiView, BooksUpdateDeleteApiView, BooksCreateApiView, BooksViewSet

router = SimpleRouter()
router.register('books', BooksViewSet, basename='books')


urlpatterns = [
    path('books/', BooksListApiView.as_view()),
    path('books/<int:pk>/', BooksDetailApiView.as_view()),
    path('books/create/', BooksCreateApiView.as_view()),
    path('books/<int:pk>/delete/', BooksDeleteApiView.as_view()),
    path('books/<int:pk>/update/', BooksUpdateApiView.as_view()),
    path('books/listcreate/', BooksListCreateApiView.as_view()),
    path('books/<int:pk>/updatedelete/', BooksUpdateDeleteApiView.as_view()),
]

urlpatterns += router.urls