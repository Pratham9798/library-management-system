from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from .tasks import generate_report

# Author ViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# BorrowRecord View
@api_view(['POST', 'PUT'])
def borrow_book(request, pk=None):
    if request.method == 'POST':
        book = Book.objects.get(pk=request.data['book'])
        if book.available_copies > 0:
            borrow_record = BorrowRecord.objects.create(
                book=book,
                borrowed_by=request.data['borrowed_by']
            )
            book.available_copies -= 1
            book.save()
            return Response({'status': 'Book borrowed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'No available copies'}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        borrow_record = BorrowRecord.objects.get(pk=pk)
        borrow_record.return_date = request.data['return_date']
        borrow_record.save()

        book = borrow_record.book
        book.available_copies += 1
        book.save()
        return Response({'status': 'Book returned successfully'}, status=status.HTTP_200_OK)


# Reports View
@api_view(['GET', 'POST'])
def reports(request):
    if request.method == 'POST':
        # Trigger the background task to generate the report
        generate_report.delay()
        return Response({'status': 'Report generation started'}, status=status.HTTP_202_ACCEPTED)
    
    if request.method == 'GET':
        # Return the latest report
        try:
            with open('reports/latest_report.json', 'r') as file:
                report = file.read()
            return Response(report, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({'error': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)
