# feedback-chatbot-with-summary

<img width="1440" alt="Screenshot 2023-11-15 at 3 25 21 AM" src="https://github.com/abhi0642/feedback-chatbot-with-summary/assets/42978183/c244bce7-3ec9-4d69-9439-c3aeaec9f958">
<img width="1369" alt="Screenshot 2023-11-15 at 3 25 31 AM" src="https://github.com/abhi0642/feedback-chatbot-with-summary/assets/42978183/603164b6-106d-4de0-a2e7-4dc25703e6f4">
<img width="1440" alt="Screenshot 2023-11-15 at 3 29 12 AM" src="https://github.com/abhi0642/feedback-chatbot-with-summary/assets/42978183/9003f079-0b36-4e07-a909-136d7eeffb1c">


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

## clone the repository

## git clone https://github.com/abhi0642/feedback-chatbot-with-summary

## Navigate to the Project Directory:

cd feedback-chatbot-with-summary

## Install Dependencies:

npm install

## Step 2: Set Up AWS Lambda Function

1. Log in to your AWS Management Console and go to the Lambda service.
2. Create a new Lambda function, choose "Author from scratch", enter a function name, and select a runtime (e.g., Node.js).
3. Configure your Lambda function, set up the execution role, and add triggers.
4. Deploy your function code.
5. Save your function.

## Step 3: Set Up REST API in API Gateway

1. In the AWS Management Console, go to the API Gateway service.
2. Choose 'REST API' and click on "Build".
3. Connect your API Gateway to the Lambda function created in Step 2.
4. Deploy your API by creating a new stage (e.g., prod).
5. Note down the API endpoint URL.

## Step 4: Set LangChain

- Integrate LangChain in your application logic. Refer to the LangChain documentation for specific steps.

## Step 5: Use OpenAI API Key

Configure the OpenAI API key in your application:

```javascript
const openai = require('openai-api');
const OPENAI_API_KEY = 'your-api-key-here';
openai.setApiKey(OPENAI_API_KEY);

## Step 6: Send Conversation and Prompt to ChatGPT API

1. Integrate the ChatGPT API in your application.
2. Process the response from ChatGPT for your chatbot.
3. Display the summarized response in your chatbot interface.

## Contributing

For any issues or contributions, please refer to the 'Issues' and 'Pull Requests' sections of this repository.
