import React from 'react';
import './DialogflowChatbot.css'; // Import the CSS file

const DialogflowChatbot = () => {
    return (
        <div className="chatbot-container">
            <iframe
                allow="microphone;"
                width="350"
                height="100%"
                src="https://console.dialogflow.com/api-client/demo/embedded/fb7bb388-5481-42eb-b8f7-4596c209166a"
                title="dialogflow-chatbot">
            </iframe>
        </div>
    );
};

export default DialogflowChatbot;
