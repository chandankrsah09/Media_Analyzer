# Social Media MediaAnalyzer Analysis
A streamlined analytics module using Langflow and DataStax to assess engagement metrics from mock social media profiles. The solution features a Streamlit web interface that enables users to interact with a LangFlow-powered flow for in-depth social media performance analysis.

## Tools Utilized:
DataStax Astra DB for database management and storage.
Langflow for creating workflows and integrating GPT for analysis.
Streamlit to provide a seamless frontend experience for LangFlow integration.
![Uploading Screenshot 2025-01-07 173345.png…]()


## Key Features:
Seamless integration with LangFlow and DataStax to provide real-time insights.
Interactive chat interface allowing users to engage with social media performance analysis.
Persistent session history, storing queries and responses, utilizing Streamlit's session_state.

Intuitive user interface delivering real-time analysis directly through LangFlow.
Setup Guide
1. Clone the Repository
bash
Copy code
git clone https://github.com/chandankrsah09
/MediaAnalyzer
cd MediaAnalyzer
2. Create a Virtual Environment
Create a Python virtual environment to manage project dependencies:

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:
bash
Copy code
source env/Scripts/activate
On Mac/Linux:
bash
Copy code
source env/bin/activate
3. Install Dependencies
Install the necessary libraries by running the following:

bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory of your project and add the following line:

dotenv
Copy code
APP_TOKEN=<your-langflow-api-token>
Replace <your-langflow-api-token> with the API token you generate from LangFlow.

5. Start the Application
Run the Streamlit application with:

bash
Copy code
streamlit run app.py

## How to Use the Application:
Type your query in the provided input area.
Click the "Generate Insights" button to initiate the analysis.
View the analysis results along with the chat history below the input area.
Directory Structure
app.py: Main Streamlit application file.
requirements.txt: Contains the project dependencies.
.env: Stores sensitive environment variables such as the LangFlow API token.
Demonstration
Check out the project demo: Watch Demo

## Important Notes:
Ensure you have a valid LangFlow API Token before running the application.
The APP_TOKEN should be stored securely in the .env file and accessed via the python-dotenv package.
