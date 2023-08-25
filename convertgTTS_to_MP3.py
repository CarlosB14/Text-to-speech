from gtts import gTTS

# --- To convert the gTTS object to a MP3 file ---

def convert_to_MP3(content, article_name):
    tts = gTTS(text=content, lang='es') 
    route = 'Python/Proyectos/Text to speech/Articulos/'+article_name+'.mp3'
    tts.save(route)
