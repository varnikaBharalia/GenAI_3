from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

# 1️⃣ Define TypedDict schema
class Review(TypedDict):
    summary: str
    sentiment: str

# 2️⃣ Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 3️⃣ Bind structured output (TypedDict)
structured_llm = llm.with_structured_output(Review)

# 4️⃣ Invoke model
result = structured_llm.invoke(
    "The hardware is great, but the software is very buggy and crashes often. "
    "There are frequent updates but they do not fix the issues. "
    "The battery life is subpar and the camera quality is mediocre."
)

# 5️⃣ Use the structured output
print(result)
print(type(result))
print(result["summary"])
print(result["sentiment"])

# # Isme ho ye raha h ki jb hum with_sturcuted_output use krte h to usme jb hum schema dete h to usme ek internally prompt egenerate hota hsystem prompt eg: - You are an AI assistant that extracts structured
# insights from text. Given a product review,
# extract: - Summary: A brief overview of the main
# points. - Sentiment: Overall tone of the review
# (positive, neutral, negative). Return the response
# in JSON format.

# ye prompt genrate hota ha ur aage mm humara review lg jata h or model ko bhej diya jata h or model se jo response ata h wo json format me ata h or usko humare defined TypedDict me convert krke deta h
