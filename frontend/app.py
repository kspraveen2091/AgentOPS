import streamlit as st

from frontend.utils.api_client import send_message


st.set_page_config(
    page_title="AgentOPS",
    page_icon="🤖",
)


st.title("🤖 AgentOPS")

st.caption("Personalized AI Agent")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Ask AgentOPS something...")


if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = send_message(user_message)

                st.write(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as e:

                st.error(f"Backend error: {e}")
