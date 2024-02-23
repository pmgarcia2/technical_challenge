# technical_challenge

Technical test consisting of two parts: one part dedicated to programming and another focused on sql.

# Description:

## First challenge (Programming)

Python is used to develop a data analysis process using the Stack Exchange API.
The process performs the following activities:
1. Connects to the link
2. Obtains the number of answered and unanswered responses
3. Get the response with the least number of views
4. Gets the oldest and the newest responses
5. Obtain the response from the owner with the highest reputation
6. Print in console from point 2 to 5

Unit tests are implemented

## Second challenge

From a database, there are tables that contain information regarding the flights that take place in Mexico

Queries are made to answer a series of questions:
1. What is the airport name that has had the most movement during the year?
2. What is the name of the airline that has made the greatest number of flights during the year?
3. On what day have there been the greatest number of flights?
4. What are the airlines that have more than 2 flights per day?

# Results:

Busiest airport: Benito Juarez and La Paz with 3 flights each.
Airline with the highest number of flights: Aeromar and Interjet with 3 flights each.
Day with the highest number of flights: 2021-02-05
Airlines with more than 2 flights per day: None, a maximum of 2 flights per day.

# Steps to run the analysis:

Clone the repository.
Install the dependencies.
Run the stackexchange_analysis.py script.
See the results in the console.

# Used technology:

Python
SQL Server

# Files:

stackexchange_analysis.py: Main script that runs the analysis.
test_functions.py: File containing the unit tests.
queries.sql: Creating tables, inserting data and queries.