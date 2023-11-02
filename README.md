# Csv_analysis_tool
This  app allows users to upload a CSV file, and you can analyse csv file with natural language query.
## Getting Started

To run this application locally, follow the steps:

1. Install the necessary packages by running:
   pip install -r requirements.txt
2. Create a file named `.env` and add the OpenAI API key

3. Run the Streamlit app by executing the command:
   streamlit run app.py

4. Open your browser and go to [http://localhost:8501](http://localhost:8501) to use the application.

## App Workflow

1. Upload a CSV file: Use the "Upload CSV file" section to upload your CSV for analysis.
2. Enter a query: Describe your query related to the DataFrame columns in the "Enter your query" text area.
3. Generate Response: Click the "Generate Response" button to produce Python Pandas code for the query based on the uploaded DataFrame's columns.

## Requirements

- Python 3.7 and above
- Install the necessary packages listed in `requirements.txt`
- OpenAI API key is required for using the GPT-3.5 model

## Author

- [Sudhanshu Rawat](https://github.com/anshudhanshu)

## Acknowledgments

- This application uses the OpenAI GPT-3.5 model for natural language processing.
- Streamlit for creating the interactive web app.



