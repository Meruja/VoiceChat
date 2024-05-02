import streamlit as st
from audio_recorder_streamlit import audio_recorder
import tempfile
import requests
import api_functional_call

st.title('🤖 Voice Assistant 🎙️')

audio_bytes = audio_recorder(
    text="Tap to start recording",
    recording_color="#ff5733",
    neutral_color="#3498db",
    icon_name="microphone-alt",
    icon_size="2x",
)

if audio_bytes:
    print(type(audio_bytes))
    
    st.audio(audio_bytes, format="audio/wav")
    
# Save audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    if st.button('🎙️Get Rsponse🎙️'):
         #Converting speech to text
        converted_text_openai = api_functional_call.speech_to_text_conversion(temp_audio_path)
        print("Transcribed text",converted_text_openai)
        st.write("Transcription:",converted_text_openai)
        textmodel_response = api_functional_call.text_chat(converted_text_openai) # Generating actor's response
        print("Response:",textmodel_response)
        audio_data = api_functional_call.text_to_speech_conversion(textmodel_response) #Convert final text response to audio format and get the audio file path

        print("Converted Text:", converted_text_openai)
        st.write("Converted Text:", converted_text_openai)
        text_model_response = api_functional_call.text_chat(converted_text_openai)  # Generating virtual assistant's response
        print("Virtual assistant's Response:", text_model_response)
        audio_data = api_functional_call.text_to_speech_conversion(text_model_response)  # Convert virtual assistant's response to audio format

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:  # Creating temporary file
            tmpfile.write(audio_data)  # Writing file contents to temporary file
            tmpfile_path = tmpfile.name
            st.write("Response:",textmodel_response)
            st.audio(tmpfile_path)





