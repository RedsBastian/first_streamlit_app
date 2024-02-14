import streamlit 
streamlit.title("nuevo texto")
streamlit.header("subtitulo")
streamlit.text("aca va el texto")
streamlit.header("🥭 Frutas🍉 ")
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
