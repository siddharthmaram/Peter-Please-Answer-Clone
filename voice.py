from gtts import gTTS, tts
from pydub import AudioSegment
import winsound


def voice(text):
    try:
        language = 'en'

        obj = gTTS(text=text, lang=language, slow=False)

        obj.save("bg_voice.mp3")

        src = "bg_voice.mp3"
        dst = "bg_voice.wav"

        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        winsound.PlaySound('bg_voice.wav', winsound.SND_ASYNC)
    except tts.gTTSError:
        pass

