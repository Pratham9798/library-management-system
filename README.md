# Library Management System API

A simple Library Management System built using Django, Django REST Framework (DRF), and Celery. This system allows users to manage books, authors, and borrow records, along with a background task to generate periodic reports on library activity.

## Features

- **Authors Management**: Create, update, list, and delete authors.
- **Books Management**: Add, update, list, and delete books.
- **Borrow Records**: Track borrowed books, including borrow and return dates.
- **Periodic Reports**: Generate and retrieve periodic reports about the library's activity.

## Technologies Used

- **Django**: For the web framework.
- **Django REST Framework**: For creating the RESTful API.
- **Celery**: For background task processing (generating periodic reports).
- **SQLite**: Default database for development.
- **Python 3.x**: Programming language.

## Setup Instructions

### Prerequisites

- Python 3.x
- Virtualenv (optional but recommended)
- Git (for version control)
- Celery with a message broker (e.g., Redis or RabbitMQ)

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
