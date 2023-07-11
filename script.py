from pydub import AudioSegment

OPENAI_KEY = os.environ["OPENAI_KEY"]
PATH = "otm070723_cms1337550_pod.mp3_ywr3ahjkcgo_2547cfdb20b60f40eb57563221685074_49570906.mp3"

START_MINUTES_PART = 16
START_SECONDS_PART = 55
START_MS = ((START_MINUTES_PART * 60) + START_SECONDS_PART) * 1000

# ends at 35:08
END_MINUTES = 35
END_SECONDS = 8
END_MS = ((END_MINUTES * 60) + END_SECONDS) * 1000

podcast = AudioSegment.from_mp3(PATH)
interview = podcast[START_MS: END_MS]





