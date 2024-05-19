# Seekers Water

## Description

Seekers Water is a Flask web application designed to facilitate job sharing within a community. Users can create an account, log in, post jobs they need done, and others can accept these jobs. The application is designed with a user-friendly interface and intuitive navigation to make the process of posting and accepting jobs as easy as possible.

## Group Members

| UWA ID | Name | GitHub Username |
|--------|------|-----------------|
| 23422858 | Aidan Power | normit581 |
| 23457938 | Daniel Raflein | danielraflein |
| 23678458 | Paul Maingi | paulmaingi |
| 23445997 | Sean Lixu | seanlixu |

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/seanlixu/CITS3403-RequestBoard.git
    ```

1. Navigate to the project directory:

    ```bash
    cd CITS3403-RequestBoard
    ```

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

1. Optionally, set up these environment variables in a `.env` file:

    ```bash
    export FLASK_APP=task_link
    export DATABASE_URL='sqlite:///:app.db'
    export FLASK_SECRET_KEY="<insert your secret key here>"
    ```

    > This will make it easier to run the application and not have to manually export the `FLASK_APP` variable each time.

1. Initialize the database:

    ```bash
    flask db init
    flask db upgrade
    ```

    > These commands will create a new database and apply the migrations in the migrations directory to the database.

1. Run the application:

    ```bash
    flask run
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
1. Register a new account or log in to your existing account.
1. To post a job, navigate to the "Post New Job" page and fill out the form with the job details.
1. To accept a job, browse the available jobs on the "Available Jobs" page and click "Apply" on a job you'd like to take on.

## Running tests

1. Navigate to the project directory:

    ```bash
    cd CITS3403-RequestBoard
    ```

1. Run the tests:

    ```bash
    python -m unittest
    ```
