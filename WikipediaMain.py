import wikipediaapi
import pyttsx3
from pydub import AudioSegment

def get_wikipedia_content(page_title, language='en'):
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(page_title)

    if not page.exists():
        print(f"Error: Wikipedia page '{page_title}' not found.")
        return None

    return page.text

def read_wikipedia_page(page_content, save_as_mp3=False):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # this will adjust the speed of the reader.

    # this will split each paragraph.
    paragraphs = page_content.split('\n')
    spoken_text = ""
    for paragraph in paragraphs:
        engine.say(paragraph)
        spoken_text += paragraph + '\n'

    engine.runAndWait()

    if save_as_mp3:
        save_to_mp3(spoken_text)

def save_to_mp3(spoken_text, output_file='output.mp3'):
    engine = pyttsx3.init()
    engine.save_to_file(spoken_text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    # enter link or title
    wikipedia_input = input("Enter Wikipedia page link or title: ")

   
    page_content = get_wikipedia_content(wikipedia_input)

    if page_content:
        # mp3 save
        save_as_mp3_input = input("Do you want to save this as an MP3 file? (y/n): ").lower()

      
        read_wikipedia_page(page_content, save_as_mp3=save_as_mp3_input == 'y')
