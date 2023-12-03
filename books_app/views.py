from .models import Books
from .serializers import BooksSerializer
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet


# class BooksListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BooksListApiView(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BooksSerializer(books, many=True).data
        data = {
            'status': 'book list',
            'books': serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)


# class BooksDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BooksDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer_data = BooksSerializer(book).data
            data = {
                'status': 'Successfully',
                'book': serializer_data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'status': "False",
                 'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND
            )

# class BooksDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BooksDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            books = Books.objects.get(id=pk)
            books.delete()
            return Response(
                {
                    'status': True,
                    'message': 'Successfully deleted'
                 }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    'status': False,
                    'message': 'Book not found'
                }, status=status.HTTP_404_NOT_FOUND
            )


# class BooksUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BooksUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        data = request.data
        serializer = BooksSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {
                'status': 'True',
                'message': 'Successfully updated'
            }, status=status.HTTP_200_OK
        )

# class BooksCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BooksCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'Books are saved to the database',
                    'books': data
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'status': 'False',
                    'message': 'Serializer in not valid'
                }, status=status.HTTP_400_BAD_REQUEST
            )



class BooksListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
