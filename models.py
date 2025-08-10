import google.generativeai as genai
from pydantic import BaseModel, Field

import streamlit as st
import json

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
from pydantic import BaseModel
from typing import List

class ReviewData(BaseModel):
    reviewer: str
    summary: str
    sentiment: str
    pros: List[str]
    cons: List[str]
    themes: List[str]
def generate_structured_review(review_text):
    prompt = f"""
You are an expert review analyst. Extract the following structured data from this review:

Review: '''{review_text}'''

Return the result in JSON format with these fields:
- reviewer
- summary
- sentiment (Positive, Negative, Neutral)
- pros (list)
- cons (list)
- themes (list)
"""
    response = model.generate_content(prompt)
    return response.text
import streamlit as st
import json

st.set_page_config(page_title="Review Analyzer", layout="wide")
st.title("📋 AI-Powered Review Analyzer")

review_input = st.text_area("Paste a product or service review here:")

if st.button("Analyze Review"):
    with st.spinner("Analyzing..."):
        raw_output = generate_structured_review(review_input)
        try:
            data = json.loads(raw_output)
            review = ReviewData(**data)

            st.success("Review analyzed successfully!")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🧑 Reviewer")
                st.write(review.reviewer)

                st.subheader("📝 Summary")
                st.write(review.summary)

                st.subheader("📈 Sentiment")
                st.write(review.sentiment)

            with col2:
                st.subheader("✅ Pros")
                st.write(review.pros)

                st.subheader("❌ Cons")
                st.write(review.cons)

                st.subheader("🎯 Themes")
                st.write(review.themes)

        except Exception as e:
            st.error("Failed to parse response. Try refining the review or prompt.")
            st.code(raw_output)

