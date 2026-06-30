# Selenium Form Automation

This project demonstrates how to automate a simple HTML form using **Python** and **Selenium WebDriver**. The automation script opens a local HTML page, fills in the required fields, submits the form, and verifies that the submission was successful.

## Features

* Automates form input
* Enters text into input fields
* Submits the form automatically
* Verifies successful form submission using an assertion
* Demonstrates basic Selenium WebDriver usage

## Project Structure

```
.
├── form.html      # HTML form used for testing
├── test.py        # Selenium automation script
└── README.md      # Project documentation
```

## Prerequisites

Before running the project, make sure you have:

* Python 3.x installed
* Mozilla Firefox installed
* Selenium installed

Install Selenium using:

```bash
pip install selenium
```

You should also have a compatible GeckoDriver available if your Selenium setup requires it.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/abdul-cel/Broadshift-QA-phase-1.git
```

2. Navigate to the project directory:

```bash
cd Broadshift-QA-phase-1
```

3. Run the automation script:

```bash
python test.py
```

## Expected Result

The script will:

1. Open the HTML form in Firefox.
2. Enter a name.
3. Enter a password.
4. Click the **Submit** button.
5. Verify that the page displays **"Received!"**.
6. Print:

```
[PASS] TEST PASSED: Form submitted successfully
```

if the test passes.

## Technologies Used

* Python
* Selenium WebDriver
* Mozilla Firefox

## Learning Objectives

This project helped practice:

* Browser automation with Selenium
* Locating web elements using different selectors
* Form interaction
* Assertions for automated testing
* Python exception handling

## Author

**Abdulazeez Khalid**
