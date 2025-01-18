import os

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
from utility import gemini_pro_vision_response
from utility import gemini_pro_response
from utility import embeddings_model_response
from utility import load_gemini_pro_model
working_dir = os.path.dirname(os.path.abspath(__file__))

#page config

st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered",
)

with st.sidebar:
    selected = option_menu('Gemini AI',
                           ['ChatBot',
                            'Image Captioning',
                            'Embed text',
                            'Ask me anything'],
                           menu_icon='robot', icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0
                           )

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

#purana chatbtot ka code hai
if selected=='ChatBot':

    model=load_gemini_pro_model()
    if "chat_session" not in st.session_state:  # Renamed for clarity
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("🤖 MAX - A ChatBot")

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_prompt = st.chat_input("Ask MAX...")
    if user_prompt:
        
        st.chat_message("user").markdown(user_prompt)

        
        gemini_response = st.session_state.chat_session.send_message(user_prompt)  # Renamed for clarity

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)


#image captioning system hai bhai 
if selected == "Image Captioning":

    st.title("📷 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_img = image.resize((800, 500))
            st.image(resized_img)

        default_prompt = "write a short caption for this image"  # change this prompt as per your requirement

        # get the caption of the image from the gemini-pro-vision LLM
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

if selected == "Embed text":

    st.title("🔡 Text to Vector")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Enter the text to get embeddings")

    if st.button("Get Response"):
        response = embeddings_model_response(user_prompt)
        st.markdown(response)


# text embedding model
if selected == "Ask me anything":

    st.title("❓ Ask me a question")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)