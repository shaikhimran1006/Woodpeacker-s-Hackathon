##"AI-Powered Data Query Interface:"
Problem Statement: Organizations often struggle with efficiently accessing and understanding client data stored in internal databases. Traditional methods of data retrieval and analysis can be time-consuming and cumbersome, leading to delays in decision-making and inefficiencies in client management. There is a need for a streamlined and intuitive solution that allows organization members to query and receive timely, accurate insights from the database through a user-friendly interface.
Prototype Objective: Develop a chat interface that leverages a Large Language Model (LLM) to read and interpret client data from an internal database. This interface will enable organization members to query the database and receive accurate, contextually relevant responses about the data.


This is an end to end LLM prototype based on Google Generative Ai API and Langchain. We are building a system that can talk to MySQL database. User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and then executing that query on MySQL database. AtliQ Tees is a T-shirt store where they maintain their inventory, sales and discounts data in MySQL database. A store manager will may ask questions such as,
•	How many white colour Adidas t shirts do we have left in the stock?
•	How much sales our store will generate if we can sell all extra-small size t shirts after applying discounts?
•	The system is intelligent enough to generate accurate queries for given question and execute them on MySQL database.
The diagram illustrates a prototype that uses an LLM (Large Language Model) to generate SQL queries based on natural language user questions.
#Key components:
•	User Question: The starting point, where a user inputs a question in natural language.
•	LLM: The first LLM processes the user question and generates an SQL query.
•	SQL Query: The generated SQL query is executed against a database.
•	Run Query: The results of the SQL query are returned.
•	LLM: A second LLM processes the query results and generates a natural language answer.
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

