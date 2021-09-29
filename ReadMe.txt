ReadMe

To make sure you can run the Python scripts, 

1. First install Python and the necessary packages
Go to python.org/download/windows, and download the latest Python release (3.9.1 on 3/2/21)
Install that and make sure that the environment variable box is checked!!! 
(Or it will refuse to acknowledge pip)

In the Terminal type:

pip install pandas (automatically installs numpy)
pip install matplotlib
pip install seaborn
pip install dataframe_image
pip install pdfkit
pip install openpyxl

Install wkhtmltopdf from wkhtmltopdf.org
Add it to the enviroment variables 
(Link if needed: https://ourcodeworld.com/articles/read/240/how-to-edit-and-add-environment-variables-in-windows-for-easy-command-line-access)

pip install wkhtmltopdf

2. Make sure that the newest 
- Survey links 2021 .xlsx file is in the folder as well as
- Overview of program courses .csv
- General pre and post survey data files, which can be downloaded from Qualtrics

Remove the timestamp from the title, and add a 0 if so that the date is always made up out of two numbers, 
Example:
2021T1_General_survey_post_February+3,+2021_14.30
Should be:
2021T1_General_survey_post_February+03,+2021


3. Run the damn thing