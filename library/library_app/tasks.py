from celery import shared_task
import json
import os
from datetime import datetime
from .models import Author, Book, BorrowRecord

@shared_task
def generate_report():
    # Generate report data
    total_authors = Author.objects.count()
    total_books = Book.objects.count()
    total_borrowed_books = BorrowRecord.objects.filter(return_date__isnull=True).count()

    report = {
        'total_authors': total_authors,
        'total_books': total_books,
        'total_borrowed_books': total_borrowed_books,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Save the report to a JSON file
    report_filename = f'reports/report_{datetime.now().strftime("%Y%m%d")}.json'
    os.makedirs(os.path.dirname(report_filename), exist_ok=True)
    
    with open(report_filename, 'w') as file:
        json.dump(report, file, indent=4)

    # Save the latest report
    with open('reports/latest_report.json', 'w') as file:
        json.dump(report, file, indent=4)
