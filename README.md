# DevPark recruitment task
This repository contains a simple application developed for a recruitment task. The application implements a basic API for exchanging currency, allowing users to check historical exchange rates effortlessly. It leverages the external **currencyapicom** SDK to seamlessly fetch accurate and up-to-date historical exchange rate data for over 170 currencies.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- Python Virtual Environment (venv)
- SQLite 3

## Technology Stack
- Python 3.10.12
- Django 5.0.2
- Django Rest Framework 3.14.0
- SQLite 3
- currencyapicom 0.1.1

  ## Getting Started
1. Clone the repository:
```
git clone https://github.com/barxtex1/DevPark-task.git
cd DevPark-task
```
2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
venv\Scripts\activate (for Windows users)
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. You can specify your **currencyapicom** API_KEY inside `backend/manifest.json` file
> NOTE: Inside the manifest file is already an API_KEY with a free plan for testing purposes only
5. Go to the project directory and run server in your local network:
```
cd backend
python manage.py runserver
```
> NOTE: You don't need to run the migrations because the db are already provided

The project will now be running at localhost.

## Project Structure

The repository is organized into two main parts:
- The `backend` directory contains all the files responsible for the API implementation
- `py_client` folder contains a simple Python script for testing the API endpoint using the `requests` library. 

## Usage
### Endpoints
- Admin Panel:
    - Access at http://localhost:8000/admin/
    - Credentials: admin:admin
- Currency List:
    - Access at http://localhost:8000/api/currencies/
    - List of all available currencies with filtering capability
- Currency exchange:
    - Access at http://localhost:8000/api/exchange/
    - Currency exchange with input parameters:
        - `input_currency`: The currency code for the input currency.
        - `output_currencies`: A comma-separated list of currency codes for the desired output currencies.
        - `amount`: The amount of the input currency for which the exchange is requested.
        - `date`: The date for which historical exchange rates are to be retrieved.
    - Example query:
        [http://localhost:8000/api/exchange/?input_currency=PLN&output_currencies=EUR,USD,AMD&amount=155.15&date=2023-12-12](http://localhost:8000/api/exchange/?input_currency=PLN&output_currencies=EUR,USD,AMD&amount=155.15&date=2023-12-12)

## Running Tests
Tests have been written for this project and can be executed using the following command:
```
python manage.py test --keepdb
```


