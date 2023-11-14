import json
import boto3
from datetime import datetime
s3_client = boto3.client('s3')
print('Loading function')
formatted_output = ""
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain import PromptTemplate, FewShotPromptTemplate
openai_api_key="sk-"


def lambda_handler(event, context):
    global formatted_output  # Declare to modify the global variable

    print("Received event:", event)
    print("Context:", context)
    body = json.loads(event['body'])
    
    end_of_conversation = False

    # Extracting question and answer
    question = body.get("queryResult", {}).get("queryText", "")
    answer = body.get("queryResult", {}).get("fulfillmentText", "")
    if question and answer:
        formatted_output += f"-----------------------\n"
        formatted_output += f"Question: \"{question}\"\n"
        formatted_output += f"Answer: \"{answer}\"\n"
        formatted_output += f"-----------------------\n"

    if "end of conversation" in answer:
        end_of_conversation = True

    if end_of_conversation:
        print("heyyyyyy",formatted_output)
        summary_of_conversation(formatted_output)
    else:
        print(formatted_output)


def summary_of_conversation(conversation_text):
    global formatted_output  # Declare to modify the global variable
    llm = OpenAI(
            model_name="gpt-4",
            temperature=0.5,
            max_retries=3,
            max_tokens=500,
            openai_api_key=openai_api_key,
            streaming=True,
        )

    prompt = """
                Given a set of customer feedback in a question-and-answer format, your task is to create a comprehensive summary of approximately 400 words.
                This summary should encapsulate the key points, concerns, praises, and overall sentiment expressed in the feedback. 
                Additionally, apply advanced sentiment analysis methods to assign a score to the overall feedback. 
                This score should reflect the general tone and sentiment of the customer responses, whether positive, negative, or neutral. 
                Consider the nuances in the language used, the intensity of the emotions expressed, and any specific aspects of the product or service that are repeatedly mentioned. 
                Your analysis should provide a clear, concise, and accurate representation of the customer's experience and satisfaction level.
                """

    chain = ConversationalRetrievalChain.from_chain_type(
            llm=llm,
            chain_type="stuff",
            return_source_documents=True,
            chain_type_kwargs=prompt
        )
    chain_response = chain(conversation_text)
    response = chain_response["answer"].strip()
    formatted_output = ""  # Clear the global variable
    store_summary_in_s3(response)
    return response


def store_summary_in_s3(summary):
    bucket_name = "summary-feedback"
    file_name = f"conversation-summary-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=summary)