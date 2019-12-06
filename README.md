# ECE 143 Final Project

## File Structure
## 1. src_py/ 

This directory contains all the individual .py files that help in cleaning, organizing, processing and plotting our data sets. The name of the files roughly indicate the function they are implementing. There are .py files for each “question” that we wished to answer with the CAPE dataset. Each .py file manipulates the data in ways that show interesting information, such as which class is considered the “best” overall and is there is a correlation between grade received and professor recommendation, Is it easier to take a course in summer, How are the enrollment trends in the ECE department? etc.

## 2. data/

This directory has all the data that we obtained and processed for the project. There is unprocessed raw data files and also cleaned and processed data files in the .csv format here. 

## 3. Cape_Analysis_Plots_Insights.ipynb
All of our visualizations are combined in the Jupyter notebook "Cape_Analysis_Plots_Insights.ipynb".

## 4. Team 21 Presentation.pdf
Has the presentation with selected interesting questions on the data set answered and interpreted.

## How to Run Code
The .py files can be ran in a terminal with the command “python3.7 <file>” where <file> is the .py file that you wish to run. The file can also be ran in the Python shell by using “import <file>”. Then type “<file>” to run the script. Include the files in data/ directory to run the individual .py files. However since all the functions are linked its easier to run them in the Jupyter Notebook which takes care of getting the files. The Juptyer notebook can be ran in the Jupyter environment.

## Third-Party Modules
We used Pandas, Numpy, and Matplotlib to manipulate and represent our data.
