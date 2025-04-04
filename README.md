### Complient Auditing Research Tool

## Overview

This is a web-based application that provides a chat-like interface for searching and retrieving program information. This will be used for client based reasearch to help QA Auditors efficiently and accurately sift through information needed for a client.

## Features

Chat Interface: User input field for search queries.

Dropdown Navigation: Users can select program sections using a dropdown menu.

## Technologies Used

HTML: Structuring the webpage.

CSS: Styling and layout (dark theme, flexbox for chat alignment).

JavaScript: Handles user input, dropdown selection, and auto-scrolling.

Python: Handling the libraries

## File Structure

/static/css/stylesheet2.css    # Styles for chat interface and dropdown
/static/js/snr.js              # Handles chat input and scrolling
index.html                     # Main structure of the web application
README.md                      # Documentation (this file)

## How to Use

Open the application in a browser.

Enter a query in the search box.

Use the dropdown to select a program section (if applicable).

Click Send or press Enter to submit the query.

The response appears in the chat window.

## Installation & Setup

1. Clone the repository:
    git clone https://github.com/CodingDos/snr.git

2. Navigate to the project folder:
    cd snr

3. Set up (venv) virtual environment:
    python -m venv venv

4. Activate virtual environment:
    source venv/bin/activate

5. Install modules:
    pip install -r requirements.txt


## Future Enhancements

Backend Integration: Connect with a real database.

User Authentication: Secure access for different users.

## License

This project is open-source under the Virgins License.