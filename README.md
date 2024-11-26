# TO-DO-Service

> TO-DO Service with Authintication
---------------------------
## Introduction

> The TO-DO Service is a RESTful web service built with Flask that allows users to manage their personal tasks efficiently. The service incorporates user authentication to ensure data privacy and security, enabling each user to maintain their own to-do list independently.
---------------------------
### Dependencies

> The TO-DO Service relies on several key technologies and libraries to ensure optimal performance and functionality. Here are the core dependencies:

- Python:

 visit (https://www.python.org/downloads/) and install latest version of python 3.11

- Flask
- Flask-RESTful
- Flask-JWT-Extended

To install these dependencies, use the package manager pip with the provided requirements.txt file:

```
pip install -r requirements.txt
```
-------------------

### Installation 

- Clone the repo file https://github.com/Maha927/TO-DO-Service.git or download zip 
- Install dependencies:
```
- pip install -r requirements.txt
```
- Apply database migrations:

```
flask db upgrade
```

- Run the development server:

```
python app.py
```

> The backend should now be accessible at http://localhost:5000/.

### Usage

> This service is ideal for developers seeking a modular and secure backend solution for task management applications. It provides a robust foundation for a wide range of use cases, including personal productivity tools, team task management, or learning platforms with assignment tracking.
