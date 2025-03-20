from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs
from voice_of_the_patient import record_audio, transcribe_with_groq
from brain_of_the_doctor import encode_image, analyze_image_with_query
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

# System prompt for AI analysis
system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes. 
What's in this image? Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also, always answer as if you are answering a real person. 
Do not say 'In the image I see' but say 'With what I see, I think you have ....' 
Do not respond as an AI model in markdown. Your answer should mimic that of an actual doctor, not an AI bot. 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away, please."""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided"

    # Convert response to speech
    output_audio_path = "doctor_response.mp3"
    text_to_speech_with_gtts(input_text=doctor_response, output_filepath=output_audio_path)

    return speech_to_text_output, doctor_response, output_audio_path


# Gradio UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)
