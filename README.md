# Django Task Tracker

Refactored into a complete Django web application for managing tasks with status/priority workflows and a JSON API.

## Features

- Create, update, view, and delete tasks
- Filter tasks by status
- Priority and due-date support
- JSON API endpoint for task list
- Django admin integration
- Automated tests for model and view behavior

## Tech Stack

- Python 3
- Django 5
- SQLite (default local database)
- Bootstrap 5 (template UI)

## Project Structure

```text
.
├── manage.py
├── requirements.txt
├── assignment_portal/
└── tasks/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── tests.py
    └── templates/tasks/
```

## Quick Start

```bash
git clone https://github.com/sakib-maho/django-task-tracker.git
cd django-task-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## API

- `GET /api/tasks/` returns JSON task data.

## Run Tests

```bash
python manage.py test
```

## License

MIT - see [LICENSE](LICENSE).
