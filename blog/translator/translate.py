from googletrans import Translator

def language(text):
    tr = Translator()
    translation = tr.translate(text=text,dest='ta')
    return translation.text

    