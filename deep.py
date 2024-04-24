import pyaudio
import wave
import keyboard

def record_audio(filename, chunk=1024, format=pyaudio.paInt16, channels=1, rate=44100):
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    print("Recording... Press Enter to stop.")

    frames = []
    while not keyboard.is_pressed('enter'):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording stopped.")

    # Stop stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save audio to file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Audio saved as '{filename}'")

# Usage
filename = "audio.wav"
record_audio(filename)
