# Django-Python-Machine-Test
# Project Name

A brief description of your project goes here. This could include the purpose of the project, its main features, and any relevant background information.

The task is to design APIS for the machine test using any REST framework

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)6
6. [Contact](#contact)

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed.
- **PostgreSQL**: The project uses PostgreSQL as the database. You need to have PostgreSQL installed and running on your machine.

### Postgres SQL 
Passwaord : P@ss123

### Superuser :- details

username : vaibhav

Email address: vaibhav123@gmail.com

Password : Testapi@123


### user 1 :- user details for api

username : vaibhav1

Email address: vaibhav43@gmail.com

Password : Testapi@123


### user 2 :- user details for api

username : admin

Email address: vaibhav1245@gmail.com

Password : Testapi#369


### Database Configuration

Before running the project, ensure you have the correct PostgreSQL configuration:

- **Database Name**: `machine_test_db`
- **Username**: `Vaibhav_123`
- **Password**: `P@ss123`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/vaibhavKulkarni26/Django-Python-Machine-Test.git
   cd machine_test_api
   ```

## Run database migrations:

   ```
   python manage.py migrate
   ```

## Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
To use the application, open your web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

# You can also use tools like Postman to interact with the API.
API Endpoints
Here are some API endpoints you can use to interact with the application:
### http://127.0.0.1:8000/api/clients/
### http://127.0.0.1:8000/api/projects/


List all clients:
GET /api/clients/

Create a new client:
POST /api/clients/

Retrieve a client:
GET /api/clients/:id

Update a client:
PUT /api/clients/:id

Delete a client:
DELETE /api/clients/:id

Create a new project:
POST /api/clients/:id/projects/

List all projects for the logged-in user:
GET /api/projects/

## Contact
For any questions, please contact:

Email : vaibhavkulkarni095@gmail.com# Django-Python-Machine-Test