import  streamlit as st
import glob
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


filepaths = glob.glob("diary/*.txt")
filepaths = sorted(filepaths)

analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()

    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)


st.header("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)


