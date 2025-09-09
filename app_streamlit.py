import streamlit as st
import numpy as np
from apputil import ways, lowest_score, sort_names

st.title("Student Scores & Coin Change App")

st.header("Ways to Make Change, Using Nickels and Pennies")
n = st.number_input("Enter cents:")
if st.button("Calculate Ways"):
    st.write(f"Ways for {n} cents: {ways(n)}")

st.header("Student Scores")
names_input = st.text_area("Enter student names (comma separated):", "Alice,Bob,Charlie,Dana,Eve")
scores_input = st.text_area("Enter scores (comma separated):", "99,62,85,62,62")

if st.button("Analyze Scores"):
    names = np.array([name.strip() for name in names_input.split(",")])
    scores = np.array([int(score.strip()) for score in scores_input.split(",")])
    lowest = lowest_score(names, scores)
    st.write(f"Students with the lowest score: {', '.join(lowest)}")
    sorted_names = sort_names(names, scores)
    st.write(f"Names sorted by score (high to low): {', '.join(sorted_names)}")
