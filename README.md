# File Entry Application

The File Entry Application is a Python-based program designed to manage job numbers and user inputs related to job records. It utilizes a combination of custom classes and configuration variables to interact with an Access database and store user inputs. The application is built using the ttkbootstrap library for a consistent and modern look.

## Table of Contents

- [Features](https://chat.openai.com/?model=gpt-4#features)
- [Installation and Setup](https://chat.openai.com/?model=gpt-4#installation-and-setup)
- [Usage](https://chat.openai.com/?model=gpt-4#usage)
- [Code Overview](https://chat.openai.com/?model=gpt-4#code-overview)
  - [job_number_generator.py](https://chat.openai.com/?model=gpt-4#job_number_generatorpy)
  - [job_number_storage.py](https://chat.openai.com/?model=gpt-4#job_number_storagepy)
  - [user_input_storage.py](https://chat.openai.com/?model=gpt-4#user_input_storagepy)
  - [config.py](https://chat.openai.com/?model=gpt-4#configpy)

## Features

- Generate new job numbers based on the current year and month.
- Store and manage job numbers (existing, active, and current year job numbers).
- Add, remove, and clear job numbers.
- Store user input objects and their values.
- Interact with an Access database to read and write job records.
- Configure application window size, database path, and column orders.

## Installation and Setup

1. Clone this repository to your local machine or download it as a zip file and extract it.
2. Ensure you have Python 3.7 or newer installed. You can download it from [Python's official website](https://www.python.org/downloads/).
3. Install the required libraries by running the following command in your terminal or command prompt:
    `pip install -r requirements.txt`
4. Update the `config.py` file to match your desired settings and database path.

## Usage

1. Run the main script `file_entry.py` to launch the application:
    `python file_entry.py`

2. Use the application to create new job numbers, manage existing job numbers, and store user inputs related to job records.

## Code Overview

### job_number_generator.py

This module contains the `JobNumberGenerator` class, responsible for generating new job numbers based on the current year and month. It can also return a job number prefix for a specified number of previous months.

### job_number_storage.py

This module contains the `JobNumbers` class, responsible for storing job numbers in various categories such as existing, active, and current year job numbers. It provides methods to add, remove, and clear job numbers, as well as to retrieve lists of job numbers in each category.

### user_input_storage.py

This module contains the `UserInputStorage` class, responsible for storing user input objects and their values. It can add input objects to its internal storage, clear the storage, and return a dictionary of input object names and their values.

### config.py

This module contains configuration variables for the application, such as the application window size, the database path, and the column order for the existing and active databases. Update this file to match your desired settings and database path.

---
For more information, refer to the source code files and comments within each module.

## Contributing

We welcome contributions to improve the File Entry Application. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Create a pull request with a description of your changes.

Please ensure that your code follows the existing style and structure. Adding comments to your changes is highly encouraged.

## Support

If you encounter any issues or have questions about the File Entry Application, please create an issue on the GitHub repository. We will do our best to address your concerns in a timely manner.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for more information.
