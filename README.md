# Todo Task Manager

A Django-based task management application that enables users to:

- Create and manage tasks
- Add comments to tasks
- Mark tasks as complete
- Django auth system (register/login)

## Setup

1. Clone the repository

```bash
git clone https://github.com/ritasermaxhaj/to_do_tasks.git
cd to_do_tasks
```

2. Create and activate virtual environment

```bash
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
.\venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply database migrations

```bash
python manage.py migrate
```

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

## Load Sample Data (Optional)

To load initial sample data:
Make sure also to manually change the user ID in the JSON file or create a user with that specific user ID

```bash
python manage.py loaddata fixtures/seed_data.json
```
