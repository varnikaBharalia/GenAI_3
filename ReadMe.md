# Structured Output 

1. In LangChain, structured output refers to the practice of having language models return
responses in a well-defined data format (for example, JSON), rather than free-form text. This
makes the model output easier to parse and work with programmatically
        refer: - langChain.pdf

2. UseCases of Structed output 

        1) Data Extraction :- resume uploaded --> text extracted --> llm --> convert this to json --> send to database --> save these data into database

        2) API Building :- We are given review of the product -> we just make the output like  topic -> , pros -> , cos-> , sentiment -> and these are stored and can be send to anybody. So that we did that we made api output using flask or fastAPI and can be send to anybody 

        3) Build Agents 

3. Ways to get Structed Output :-

        1) LLMs that alredy generate stuctured  --> with_structed_output
        2) LLMs that can't --> OutpurParser - clases written in langChain that are used to give stucred output 


4. With_structed_output :- just use it before the model.invoke with dta format that you want 

        1) Type dict

        2) Pydantic 

        3) JSON_schema

5. TypedDict is a way to define a dictionary in Python where you specify what keys and values
should exist. It helps ensure that your dictionary follows a specific structure.

6. Why use TypedDict?
• It tells Python what keys are required and what types of values they should have.
• It does not validate data at runtime (it just helps with type hints for better coding)

        It doesn't throw any error if you take wrong data type. 

7. With_structed_output TypeDict:-

        1) Intialised the LLM

        2) Define schema

        3) bind schema with the sturded_output

        4) invoke model

        5) get sturdted output 

8 .  Annotated typeDict:- Annotated TypedDict is used to provide semantic guidance to LLMs while keeping strict structural typing, improving accuracy in structured output extraction.
         
        | Benefit                     | Explanation                      |
| --------------------------- | -------------------------------- |
| 🧠 Better LLM understanding | Model knows *how* to fill fields |
| 📐 More accurate output     | Fewer hallucinations             |
| 🔒 Better schema alignment  | Less chance of tool-call errors  |


9 . Pydantic :- this is used for the data validation 