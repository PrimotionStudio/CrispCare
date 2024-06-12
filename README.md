# CrispCare

CrispCare is a house care service application designed to manage and register house help services.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Overview

CrispCare simplifies the process of managing house help services by providing an easy-to-use platform for registering, searching, and managing house help profiles.

## Features

- **House Help Registration**: Easily register new house helps with details such as name, age, services offered, and rating.
- **Service Management**: Manage and view available services offered by house helps.
- **User-Friendly Interface**: Simple and intuitive interface for both administrators and users.

## Installation

To install and run CrispCare locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/PrimotionStudio/CrispCare.git
    cd CrispCare
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the application, run:

```sh
python3 -m main.py
```

### Using the application

To start using crisp care, visit `http://localhost:5000` on your browser


## Project Structure

- `main.py`: The main entry point for the application.
- `requirements.txt`: Lists the dependencies required to run the application.
- `README.md`: Provides information about the project.
- `static/`: Contains static files such as CSS and JavaScript.
- `templates/`: Contains HTML templates for the web interface.
- `app/`: Contains the application logic and routes.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL (SQLAlchemy)

## API Endpoints

- `POST /api/register_househelp`: Register a new house help.
- `GET /api/househelps`: Retrieve a list of all registered house helps.
- `GET /api/househelp/<id>`: Retrieve details of a specific house help by ID.

## Contributing

We welcome contributions to the CrispCare project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
