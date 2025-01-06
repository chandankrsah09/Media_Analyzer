import requests
import json
import streamlit as st

# Access APP_TOKEN from Streamlit Secrets
APP_TOKEN = st.secrets["astra"]["APP_TOKEN"]  # Use the secret key you set in Streamlit Secrets

if not APP_TOKEN:
    raise ValueError("Streamlit secret APP_TOKEN is not set. Please check your Streamlit secrets.")

# Base configurations
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "19cdce06-0856-4984-910b-3df678dab0fb"
FLOW_ID = "ccd9a8f8-f3a9-4fb7-9267-776d5bf61e67"
ENDPOINT = "predict"

# Function to run the flow
def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {
        "Authorization": f"Bearer {APP_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)

    # Check for errors in the response
    if response.status_code != 200:
        raise ValueError(f"API request failed with status code {response.status_code}: {response.text}")

    return response.json()

# Main function
def main():
    st.title("Social Media Performance Analysis")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Input field for the user
    message = st.text_area("Enter your message:", placeholder="How can we assist you today?")

    # Button to send the query
    if st.button("Generate Insights"):
        if not message.strip():
            st.error("Please enter a message.")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
                response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

            # Append user message and response to chat history
            st.session_state["messages"].append({"user": message, "bot": response_text})

        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Display a chat history
    st.subheader("Chat History")
    for chat in st.session_state["messages"]:
        st.markdown(f"*You:* {chat['user']}")
        st.markdown(f"*Bot:* {chat['bot']}")
        st.divider()

if __name__ == "__main__":
    main()
