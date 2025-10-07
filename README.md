# Dynamic Dashboard with Flask and Docker

This project demonstrates a dynamic web dashboard built with **Flask** that reads data from Excel (`.xlsx`) or CSV files and displays it interactively on a web interface. The application is containerized using **Docker** for easy deployment and portability.

---

## Project Structure

.
├── app.py # Flask backend application
├── Dockerfile # Docker configuration for containerization
├── index.html # Frontend template for dashboard
├── requirements.txt # Python dependencies
├── Change Activity Tracking Sheet.xlsx # Sample data file
└── README.md # Project documentation

yaml
Copy code

---

## Features

- Reads data from `.xlsx` or `.csv` files.
- Dynamic and interactive web dashboard.
- Simple Flask backend to serve data and templates.
- Fully containerized with Docker for easy deployment.
- Modular design for easy integration of new datasets.

---

## Prerequisites

Make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- Optional: [pip](https://pip.pypa.io/en/stable/installation/) for local testing

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Python dependencies (optional if using Docker):

bash
Copy code
pip install -r requirements.txt
Running Locally (Without Docker)
Ensure the data file Change Activity Tracking Sheet.xlsx is in the project directory.

Run the Flask app:

bash
Copy code
python app.py
Open your browser and navigate to:

cpp
Copy code
http://127.0.0.1:5000
Running with Docker
Build the Docker image:

bash
Copy code
docker build -t flask-dashboard .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 flask-dashboard
Open your browser and navigate to:

arduino
Copy code
http://localhost:5000
Usage
The dashboard reads the Excel/CSV file and displays data in a table or interactive charts.

Modify the Change Activity Tracking Sheet.xlsx file to update the dashboard dynamically.

Frontend customization can be done via index.html and Flask routes in app.py.

Requirements
Flask

pandas

openpyxl (for reading .xlsx files)

Other dependencies listed in requirements.txt

Notes
Make sure your data file format matches the columns expected in app.py.

Docker ensures the app runs consistently across different environments.

You can extend this project by adding filters, charts, and other visualizations.
