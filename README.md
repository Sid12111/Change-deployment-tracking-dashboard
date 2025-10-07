# **📊 Dynamic Activity Dashboard (Flask & Docker)**

## **Project Overview**

This project provides a dynamic, web-based dashboard for visualizing activity data sourced from a static Excel (.xlsx) or CSV file. The backend is built using **Flask**, a lightweight Python web framework, which handles data loading, processing (using Pandas), and serving the data to the frontend. The entire application is containerized using **Docker** for easy deployment and portability.

The primary goal is to transform raw activity data from the source file (Change Activity Tracking Sheet.xlsx) into an interactive visualization accessible via a web browser.

## **✨ Features**

* **Dynamic Data Loading:** Automatically reads data from the specified xlsx/csv file upon startup.  
* **Flask Backend:** Simple and scalable RESTful structure to serve HTML and data endpoints.  
* **Responsive Frontend:** Displays data in a clean, dynamic web interface (using index.html).  
* **Containerized Deployment:** Includes a Dockerfile for single-command build and deployment in any Docker environment.  
* **Real-time Updates (Simulated):** The dashboard refreshes based on the latest data in the source file when the application is restarted.

## **📁 Project Structure**

This repository is structured as follows:

.  
├── Change Activity Tracking Sheet.xlsx \# Your primary data source  
├── Dockerfile                  \# Instructions for building the Docker image  
├── README.md                   \# This file  
├── app.py                      \# Flask application: loads data and serves the dashboard  
├── index.html                  \# Frontend template for the dashboard UI  
└── requirements.txt            \# Python dependencies (Flask, Pandas, etc.)

## **⚙️ Setup and Installation**

### **1\. Prerequisites**

You must have the following installed on your system:

* **Python 3.8+**  
* **pip** (Python package installer)  
* **Docker** (Recommended for deployment)

### **2\. Local Development Setup**

To run the dashboard directly on your machine:

1. **Clone the repository:**  
   git clone \[your-repo-link\]  
   cd \[your-repo-name\]

2. Install dependencies:  
   The necessary Python libraries (like Flask and Pandas) are listed in requirements.txt.  
   pip install \-r requirements.txt

3. Prepare your data file:  
   Ensure your activity data is present in the root directory and named exactly: Change Activity Tracking Sheet.xlsx.  
4. **Run the Flask application:**  
   python app.py

   The application will typically be accessible at http://127.0.0.1:5000/.

### **3\. Docker Deployment (Recommended)**

To run the application inside a container for maximum portability:

1. **Ensure your data file is in the root directory.** The Dockerfile assumes Change Activity Tracking Sheet.xlsx is present.  
2. Build the Docker image:  
   This command uses the instructions in the Dockerfile to create a named image.  
   docker build \-t activity-dashboard:latest .

3. Run the Docker container:  
   This command starts the container and maps the internal port 5000 to external port 8080 on your host machine.  
   docker run \-d \-p 8080:5000 \--name dashboard-app activity-dashboard:latest

4. Access the dashboard:  
   Open your web browser and navigate to http://localhost:8080.

## **💻 Core Files Explained**

### **app.py**

This is the heart of the application. It uses the pandas library to read the data from the Excel file and converts it into a structured format (JSON) that can be consumed by the frontend. It defines routes, including the main route (/) which renders index.html.

### **index.html**

The single-page frontend template. It will use JavaScript (e.g., Fetch API) to communicate with the Flask backend routes defined in app.py, retrieve the activity data, and dynamically populate the dashboard elements (tables, charts, etc.).

### **Dockerfile**

A multi-stage build file that sets up a clean, minimal Linux environment, installs Python, copies the source code and data, installs dependencies from requirements.txt, and finally runs app.py. It ensures your application runs consistently everywhere.

Enjoy visualizing your data\!
