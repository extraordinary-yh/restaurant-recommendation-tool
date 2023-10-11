# Choose Your Dream Restaurant: A Prolog-Python Hybrid Application

## Overview

This application is designed to help users find a restaurant that best suits their preferences. It uses a combination of Python and Prolog to ask a series of questions and then recommends a restaurant based on the user's answers.

## Requirements

- Python 3.x
- PySWIP package
- A Prolog knowledge base (KB) containing facts and rules about restaurants (not shown in the code snippet)

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install PySWIP using pip:
    ```bash
    pip install pyswip
    ```

## How It Works

1. The application initializes a Prolog interpreter through PySWIP.
2. It then asks the user a series of questions about their preferences, such as cuisine, diet, activity, distance, number of people, budget, atmosphere, and outdoor sitting.
3. The user's answers are used to query the Prolog knowledge base.
4. Finally, the application recommends a restaurant based on the query results.

### Functions

- `write_py(X)`: Writes the options for each question to the console.
- `read_py(A, Ans, Menu)`: Reads the user's input for each question and unifies it with a Prolog variable.

### Prolog Interaction

The code uses PySWIP to interact with a Prolog interpreter. It consults a Prolog knowledge base (not shown in the code snippet) to make its recommendations.

## Usage

1. Make sure you have a Prolog knowledge base file that contains facts and rules about restaurants.
2. Run the Python script.
3. Answer the questions as prompted.

## Output

The application will recommend a restaurant based on your answers. If it can't find a suitable restaurant, it will inform you that you're on your own.
