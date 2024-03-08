# Gemini Pro - ChatBot

Gemini Pro is a powerful chatbot built with Streamlit and powered by Google's Generative AI model. It provides an interactive chat interface, where users can ask questions and receive answers dynamically. This project demonstrates the integration of Google's Generative AI with a Streamlit web application to create an engaging user experience.

## Features

- Interactive chat interface powered by Google's Generative AI.
- Ability to reset chat history directly from the web interface.
- Dark theme for a modern and comfortable user experience.

## Installation

Before you begin, ensure you have Python installed on your system.

1. Clone the repository to your local machine:

```
git clone https://github.com/anayy09/Gemini-Pro-ChatBot.git
```

2. Navigate to the project directory:

```
cd Gemini-Pro-ChatBot
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```

This is necessary for the chatbot to communicate with Google's Generative AI services.

5. Run the Streamlit app:

```
streamlit run main.py
```

The application will start, and you can access it through your web browser.

## Usage

After launching the application, use the interactive chat interface to communicate with the Gemini Pro chatbot. Type your questions or messages into the chat input field, and the chatbot will respond.

- To reset the chat history, use the "Reset Chat" button located in the sidebar.
- The sidebar also contains a feedback form where you can share your experience with Gemini Pro.

## Contributing

We welcome contributions to Gemini Pro! If you have suggestions for improvements or encounter any issues, please open an issue first to discuss what you would like to change. For direct contributions, please submit a pull request.

## Hosting

Gemini Pro is currently hosted and accessible at [https://anays-gemini-pro.streamlit.app/](https://anays-gemini-pro.streamlit.app/). Visit the link to interact with the live version of the chatbot.
