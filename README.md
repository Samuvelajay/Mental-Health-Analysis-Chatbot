# Mental-Health-Analysis-Chatbot
The Mental Health Analysis Chatbot is a web application that uses NLP and Machine Learning to detect mental health conditions from user input. It provides a chatbot interface where users can share their thoughts, and the chatbot predicts mental health statuses like Normal, Depression, Suicidal, Anxiety, Stress, Bi-Polar, or Personality Disorder.

Objectives:
Detect potential mental health issues from user messages.
Provide personalized insights based on text analysis.
Maintain a record of conversations and predictions for analysis and future reference.

Technologies Used:
Machine Learning: Uses a trained model (e.g., Logistic Regression) to classify text data into mental health categories.
NLP Techniques: Includes text preprocessing, sentiment analysis, and classification.

Flask: Backend framework to create a web application for user interaction.
SQLite: Database to store user conversations and predictions.
HTML/CSS: Frontend design for the chatbot interface.

Features:
User Registration: Takes the user’s name and phone number.
Chat Interface: Allows users to input text messages.
Prediction: Uses the trained model to classify the mental health status.
Data Storage: Stores user details, chat messages, and predictions in an SQLite database.
Interactive Interface: Provides a conversational experience for the user.

Workflow:
User enters their name and phone number on the homepage.
The chatbot page is displayed where the user can chat with the system.
The model processes the input text and predicts the mental health category.
The prediction, along with the message, is stored in the SQLite database.
The chatbot displays the prediction in the chat interface.
