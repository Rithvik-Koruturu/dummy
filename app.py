import streamlit as st
import requests
import openai  # If you're using OpenAI GPT or another similar model

# Setup your OpenAI or Gemini model API key (adjust depending on the AI model you are using)
API_KEY = "YOUR_API_KEY"
openai.api_key = API_KEY

# Streamlit app layout
st.title("AI Sales Copilot")

# Input fields for the sales representative
st.header("Customer Interaction")

# Customer email input
customer_email = st.text_area("Enter Customer's Email", "", height=200)

# Customer profile and sales stage
st.subheader("Sales Details")
customer_name = st.text_input("Customer Name")
deal_stage = st.selectbox("Sales Stage", ["Initial Contact", "Discovery", "Negotiation", "Final Decision"])

# Function to interact with the AI (GPT-3/4 or Gemini model API)
def get_ai_response(email_content, customer_name, deal_stage):
    prompt = f"""
    You are an AI sales assistant. Based on the following customer email and deal stage, generate a personalized response:

    Customer Name: {customer_name}
    Sales Stage: {deal_stage}

    Customer Email:
    {email_content}

    Provide a response that acknowledges the customer's concerns, provides value, and moves the deal forward.
    """

    try:
        # Making an API request to OpenAI or Gemini (adjust the URL depending on your model)
        response = openai.Completion.create(
            engine="text-davinci-003",  # Change to the correct model like "gpt-4" if needed
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7
        )

        return response.choices[0].text.strip()

    except Exception as e:
        st.error(f"Error with AI API request: {e}")
        return None


# Button to trigger AI response generation
if st.button("Generate Response"):
    if customer_email and customer_name:
        with st.spinner("Generating response..."):
            # Get AI-generated response
            ai_response = get_ai_response(customer_email, customer_name, deal_stage)
            if ai_response:
                st.subheader("Suggested Response:")
                st.write(ai_response)
            else:
                st.warning("No response generated. Please try again.")
    else:
        st.warning("Please enter both customer email and name.")
