from click import prompt
from langchain.prompts import PromptTemplate

# You are a management assistant with a specialization in diabetes and endocrine disease. 
# You are takingnotes for a meeting.
# Write a detailed summary of the following transcript of a meeting:
    
prompt_template= """

You are a highly skilled AI trained in language comprehension and summarization.
I would like you to read the following text and summarize it into a concise abstract paragraph.
Aim to retain the most important points,
providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text.
Please avoid unnecessary details or tangential points.
 
Summary in korean
------------
{text}
------------
CONSCISE SUMMARY:
"""
prompt_template = PromptTemplate(
    template=prompt_template, 
    input_variables=["text"],
)

# refine_template = (
#     "Your job is to produce a final summary\n"
#     "We have provided an existing summary up to a certain point: {existing_answer}\n"
#     "We have the opportunity to refine the existing summary"
#     "(only if needed) with some more context below.  \n"
#     "------------\n"
#     "{text}\n"
#     "------------\n"
#     "Given the new context, refine the original summary within a meeting report form and"
#     "summary some keypoints from original text in korean."
#     )

refine_template = (
    "너는 회사 기획실 실무자이고 너의 역할은 임원 회의의 회의록을 작성하는 것이야.\n"
    "1차 정리한 내용은 다음과 같아: {existing_answer}\n"
    "더 많은 컨텍스트를 통해 기존 요약을 정리할 수 있어. 단 1000자 이내에서 정리해줘."
    "(필요한 경우에만) 아래에 더 많은 컨텍스트가 제공됩니다.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "전체적인 컨텍스트를 고려해서 회의록 형식의 보고서를 작성해줘."
    "원래 텍스트에서 핵심 포인트는 별도로 요약 정리해줘."
    )


refine_prompt = PromptTemplate(
    template=refine_template,
    input_variables=["existing_answer", "text"],
)
