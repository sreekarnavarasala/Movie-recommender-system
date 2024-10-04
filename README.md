# Movie-recommender-system
This repository will focus on building movie recommender system using LLMs
**Prerequisites**

Ensure you have Python installed (https://www.python.org/downloads/).
Install the required libraries:
Bash
pip install streamlit google-generativeai langchain langchain-google-genai dotenv
Use code with caution.

**Configuration**

Create a file named .env in the root directory of your project to store your Google API key securely. Add a line like:
GOOGLE-API-KEY=YOUR_API_KEY
Replace YOUR_API_KEY with your actual Google Cloud API key, obtainable from the Google Cloud Console (https://console.cloud.google.com/).
Running the Application

Open a terminal or command prompt and navigate to the project directory.
Run:
Bash
streamlit run app.py  # Replace 'app.py' with your main script name if different
Use code with caution.

This will launch the Streamlit app in your web browser, typically at http://localhost:8501.
Usage

Enter a movie title, genre, or keyword in the text input field provided on the application page.
Click anywhere on the page outside the text input field or press Enter.
The application will generate a list of movie recommendations based on your input.
Deployment (Optional)

Consider deploying the app to a cloud platform like Heroku or Google Cloud Run for public access.
Refer to the documentation of your chosen platform for deployment instructions.
Contributing

We welcome contributions to this project! Please create a pull request on GitHub with your changes.