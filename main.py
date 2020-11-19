import os
import random
import uuid
import pyphen
from pydub import AudioSegment


char = input("Enter character name: ")
print("Will generate for", char)

script = input("Enter script: ")


filenames = os.listdir("./" + char)
voice_clips = []
for file in filenames:
    voice_clips.append(AudioSegment.from_wav("./" + char + "/" + file))
space = AudioSegment.from_wav("./common/space.wav")
pause = AudioSegment.from_wav("./common/pause.wav")


slicer = pyphen.Pyphen(lang = "nl_NL")
syllables = slicer.inserted(script).replace(" -", " ")
syllables = syllables.replace(", ", ",-")
syllables = syllables.replace(". ", ".-")
syllables = syllables.replace(" ", " -")


result = voice_clips[random.randint(0, len(voice_clips) - 1)]
for syllable in syllables:
    if syllable == " ":
        result = result + space
    elif syllable in [",", ".", "?", "!"]:
        result = result + pause
    elif syllable == "-":
        result = result + voice_clips[random.randint(0, len(voice_clips) - 1)]

result.export("output/" + char + str(uuid.uuid4().hex) + ".wav", format="wav")
