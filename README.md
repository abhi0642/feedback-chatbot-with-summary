# feedback-chatbot-with-summary



# Feedback Chatbot with Summary

Welcome to the "Feedback Chatbot with Summary" project! This chatbot is designed to collect feedback through conversation and provide a summarized response. It's built using React, AWS Lambda, API Gateway, LangChain, and OpenAI's GPT-3 API. Below are the detailed steps to set up and run this project.

## Prerequisites

Before you start, ensure you have the following:
- [Node.js and npm](https://nodejs.org/en/download/)
- [An AWS account](https://aws.amazon.com/)
- [An OpenAI API key](https://beta.openai.com/signup/)

## Installation and Setup

### Step 1: Install React and Clone the Repository

1. **Install React**:
   ```bash
   npm install -g create-react-app

git clone

git clone https://github.com/abhi0642/feedback-chatbot-with-summary

Navigate to the Project Directory:

cd feedback-chatbot-with-summary

Install Dependencies:

npm install

Step 2: Set Up AWS Lambda Function
Log in to your AWS Management Console and go to the Lambda service.
Create a new Lambda function, choose "Author from scratch", enter a function name, and select a runtime (e.g., Node.js).
Configure your Lambda function, set up the execution role, and add triggers.
Deploy your function code.
Save your function.

Step 3: Set Up REST API in API Gateway
In the AWS Management Console, go to the API Gateway service.
Choose 'REST API' and click on "Build".
Connect your API Gateway to the Lambda function created in Step 2.
Deploy your API by creating a new stage (e.g., prod).
Note down the API endpoint URL.

Step 4: Set LangChain
Integrate LangChain in your application logic. Refer to the LangChain documentation for specific steps.

Step 5: Use OpenAI API Key
Configure the OpenAI API key in your application:

const openai = require('openai-api');
const OPENAI_API_KEY = 'your-api-key-here';
openai.setApiKey(OPENAI_API_KEY);

Step 6: Send Conversation and Prompt to ChatGPT API
Integrate the ChatGPT API in your application.
Process the response from ChatGPT for your chatbot.
Display the summarized response in your chatbot interface.
Contributing

For any issues or contributions, please refer to the 'Issues' and 'Pull Requests' sections of this repository.
