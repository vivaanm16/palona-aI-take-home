import streamlit as st
import json
from main import run_pipeline

st.title("NovaMind AI Marketing Pipeline")

if "run_done" not in st.session_state:
    st.session_state.run_done = False

if "topic" not in st.session_state:
    st.session_state.topic = ""

topic = st.text_input("Enter blog topic")

if st.button("Run Pipeline"):
    if topic:
        run_pipeline(topic)
        st.session_state.run_done = True
        st.session_state.topic = topic
        st.success("Pipeline completed!")

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return None

if st.session_state.run_done:

    content = load_json("data/content.json")
    metrics = load_json("data/metrics.json")

    st.header("Results")

    if content:
        st.subheader("Blog")
        st.write(content["blog"]["title"])
        st.write(content["blog"]["content"])

        st.subheader("Newsletters")
        st.json(content["newsletters"])

    if metrics:
        st.subheader("Metrics")
        st.json(metrics)