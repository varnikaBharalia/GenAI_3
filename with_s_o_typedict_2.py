from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Optional, TypedDict ,  Annotated , Literal

load_dotenv()

# 1️⃣ Define TypedDict schema
class Review(TypedDict): 

    key_themes : Annotated[list[str] , "Write down all the key themes discussed in the review"]
    summary: Annotated[str, "A brief overview of the main points"]  
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review (positive, neutral, negative)"]
    pros: Annotated[Optional[list[str]], "List the pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List the cons mentioned in the review"]
    name : Annotated[Optional[str], "Write the name of reviewer"]


# 2️⃣ Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# 3️⃣ Bind structured output (TypedDict)
structured_llm = llm.with_structured_output(Review , strict=True)

# 4️⃣ Invoke model
result = structured_llm.invoke(
   """ I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
"""
)

# 5️⃣ Use the structured output
print(result)
print(type(result))
print(result["summary"])
print(result["sentiment"])
print(result.keys())

# # Isme ho ye raha h ki jb hum with_sturcuted_output use krte h to usme jb hum schema dete h to usme ek internally prompt egenerate hota hsystem prompt eg: - You are an AI assistant that extracts structured
# insights from text. Given a product review,
# extract: - Summary: A brief overview of the main
# points. - Sentiment: Overall tone of the review
# (positive, neutral, negative). Return the response
# in JSON format.

# ye prompt genrate hota ha ur aage mm humara review lg jata h or model ko bhej diya jata h or model se jo response ata h wo json format me ata h or usko humare defined TypedDict me convert krke deta h
