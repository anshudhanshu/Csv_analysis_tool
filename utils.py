import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import openai



import pandas as pd

prompt = """
              You will be given Natural language question name of the columns present in the dataframe. You need to generate the python pandas  code for that query.
              Query: {query}\n
              Columns: {columns}\n

              Your code sould be correct. Do not make any assumption and your code should be in one line. Do not return all the columns only return relevent columns

            """

def generate_completion(prompt, model="gpt-3.5-turbo", max_tokens=1000, temperature=0):

    # Create a list of message objects with the user's prompt
    messages = [
        {"role": "system", "content": "You are a talented data scientist having strong knowledge in python specifically pandas library."},
        {"role": "user", "content": prompt},
    ]

    # Call the OpenAI API to generate a completion
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    # Extract and return the generated text from the API response
    return response['choices'][0]['message']['content']
