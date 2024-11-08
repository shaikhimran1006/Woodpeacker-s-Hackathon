# AI-Powered Data Query Interface

## Problem Statement
Organizations often struggle with efficiently accessing and understanding client data stored in internal databases. Traditional methods of data retrieval and analysis can be time-consuming and cumbersome, leading to delays in decision-making and inefficiencies in client management. There is a need for a streamlined and intuitive solution that allows organization members to query and receive timely, accurate insights from the database through a user-friendly interface.

## Prototype Objective
Develop a chat interface that leverages a Large Language Model (LLM) to read and interpret client data from an internal database. This interface will enable organization members to query the database and receive accurate, contextually relevant responses about the data.

This is an end-to-end LLM prototype based on **Google Generative AI API** and **LangChain**. We are building a system that can communicate with a MySQL database. Users can ask questions in natural language, and the system generates answers by converting those questions into SQL queries and executing them on the MySQL database.

### Example Use Case
AtliQ Tees, a T-shirt store, maintains its inventory, sales, and discount data in a MySQL database. A store manager might ask:
- **How many white Adidas T-shirts do we have left in stock?**
- **What would our sales revenue be if we sold all extra-small T-shirts after applying discounts?**

The system intelligently generates accurate SQL queries for given questions and executes them on the MySQL database.

## System Architecture
The diagram illustrates a prototype that uses an LLM to generate SQL queries based on natural language user questions.

### Key Components:
1. **User Question**: The starting point where a user inputs a question in natural language.
2. **LLM**: Processes the user question and generates an SQL query.
3. **SQL Query**: The generated SQL query is executed against a database.
4. **Run Query**: The results of the SQL query are returned.
5. **LLM**: A second LLM processes the query results and generates a natural language response.
6. **Database Schema**: The structure of the database, used by the LLM to generate accurate SQL queries.

### Purpose
This system effectively allows users to interact with a database using natural language, simplifying the process of retrieving information.

## Technology Stack
We are using the **Streamlit** library for interface design. Streamlit is a Python library that empowers data scientists to create stunning web applications with minimal effort. It is designed to be user-friendly, allowing you to focus on data analysis and visualization while Streamlit handles the complexities of building a web interface.

### Key Features of Streamlit:
- **Simplicity**: Write Python scripts to create interactive apps.
- **Speed**: Develop and deploy applications rapidly.
- **Flexibility**: Integrate with various data science libraries like NumPy, Pandas, Matplotlib, etc.
- **Interactivity**: Create engaging apps with widgets like sliders, buttons, and selectors.

## Project Structure
processes the query results and generates a natural language answer.
•	Database Schema: The structure of the database, used by the LLM to generate the SQL query.

We are using the Streamlit library for interface design
Streamlit is a Python library that empowers data scientists to create stunning web applications with minimal effort. It's designed to be incredibly user-friendly, allowing you to focus on your data analysis and visualization while Streamlit handles the complexities of building a web interface.

#Key Features:
•	Simplicity: Write Python scripts to create interactive apps.
•	Speed: Develop and deploy applications rapidly.
•	Flexibility: Integrate with various data science libraries (NumPy, Pandas, Matplotlib, etc.).
•	Interactivity: Create engaging apps with widgets like sliders, buttons, and selectors.

#Project Structure :
•	main.py: The main Streamlit application script.
•	langchain_helper.py: This has all the langchain code
•	requirements.txt: A list of required Python packages for the project.
•	few_shots.py: Contains few shot prompts
•	.env: Configuration file for storing your Google API key.

## Setup
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run main.py`


