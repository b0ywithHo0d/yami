import streamlit as st
import openai

st.set_page_config(page_title="GPT-4.0 Mini QA", page_icon="🤖")

# --- OpenAI API Key 입력 받기 ---
api_key = st.text_input("Enter your OpenAI API key", type="password")

# --- session_state에 저장 ---
if api_key:
    st.session_state['api_key'] = api_key

# --- 질문 입력 ---
question = st.text_input("Ask a question to GPT-4.0 Mini")

@st.cache_data
def ask_gpt(question, api_key):
    if not question:
        return "Please enter a question."

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",  # gpt-4.0-mini로 알려진 모델
            messages=[
                {"role": "user", "content": question}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# --- 결과 출력 ---
if st.button("Submit") and question and 'api_key' in st.session_state:
    response = ask_gpt(question, st.session_state['api_key'])
    st.markdown("### Response")
    st.write(response)
