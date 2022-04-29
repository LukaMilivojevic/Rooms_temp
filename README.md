# Rooms_temp
Project for Teclado blog

## Quickstart

Create a `.env` file with a `DATABASE_URL` variable that points to a PostgreSQL database. Look at `.env.example` for information on how this should be written.

Create a Python virtual environment:

```
python3.10 -m venv .venv
```

Activate the virtual environment and install the dependencies using `pip`:

```
source .venv/bin/activate  # different on Windows
pip install -r requirements.txt
```

Run the app:

```
flask run
```