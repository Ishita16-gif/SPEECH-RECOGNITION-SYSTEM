import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Say something...")
        recognizer.adjust_for_ambient_noise(source)  # optional
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("⚠️ Could not request results from Google API.")

if __name__ == "__main__":
    recognize_speech_from_mic()