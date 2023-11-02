from dotenv import load_dotenv
from utils import *

if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['OPENAI_API_KEY'] =''
# Sidebar to capture the API keys
st.sidebar.title("😎🗝️")
st.session_state['OPENAI_API_KEY']= st.sidebar.text_input("Please enter your OpenAI api Key?",type="password")
st.sidebar.write("Don't have API key? Get one from [here🔗](https://platform.openai.com/account/api-keys)")

st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

# Capture the CSV file
data = st.file_uploader("Upload CSV file",type="csv")
if data:
    df = pd.read_csv(data)
    columns = list(df.columns)
query = st.text_area("Enter your query")
button = st.button("Generate Response")


if button:
    # Get Response
    if st.session_state['OPENAI_API_KEY'] !="":
        code = eval(generate_completion(prompt=prompt.format(query = query,columns=columns)))
        st.write("👉**Result :")
        st.write(code)
    else:
        st.sidebar.error("Ooopssss!!! Please provide API keys.....")