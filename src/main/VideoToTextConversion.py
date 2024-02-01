import subprocess
import speech_recognition as sr

def extract_audio(video_file, output_audio_file):
    # Run FFmpeg command to extract audio from the video file
    subprocess.call(['ffmpeg', '-i', video_file, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', output_audio_file])

def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    # Load the audio file
    audio = sr.AudioFile(audio_file)

    # Initialize an empty string to store the transcribed text
    transcribed_text = ""

    # Process the audio file
    with audio as source:
        audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        transcribed_text = recognizer.recognize_google(audio_data)
        print("Transcription:")
        print(transcribed_text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    video_file = "TOP 10 STOCKS For 2024 .mp4"  # Update with your video file path
    audio_file = "output_audio.wav"  # Output audio file path
    extract_audio(video_file, audio_file)
    convert_audio_to_text(audio_file)