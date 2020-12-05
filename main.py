import os
import random
import uuid
import pyphen
from pydub import AudioSegment

more = "yes"
while more == "yes" or more == "Yes" or more == "y" or more == "Y":
    char = input("Enter character name: ")
    print("Will generate for", char)

    script = input("Enter script: ")


    filenames = os.listdir("./voices/" + char)
    voice_clips = []
    for file in filenames:
        voice_clips.append(AudioSegment.from_wav("./voices/" + char + "/" + file))
    space = AudioSegment.from_wav("./common/space.wav")
    pause = AudioSegment.from_wav("./common/pause.wav")


    slicer = pyphen.Pyphen(lang = "nl_NL")
    syllables = slicer.inserted(script).replace(" -", " ")
    syllables = syllables.replace(", ", ",-")
    syllables = syllables.replace(". ", ".-")
    syllables = syllables.replace(" ", " -")


    random.shuffle(voice_clips)
    index = 0
    result = voice_clips[index]
    index = index + 1
    for syllable in syllables:
        if syllable == " ":
            result = result + space
        elif syllable in [",", ".", "?", "!"]:
            result = result + pause
        elif syllable == "-":
            result = result + voice_clips[index]
            index = index + 1
            if index >= len(voice_clips):
                random.shuffle(voice_clips)
                index = 0

    result.export("output/" + char + "-" + script + str(uuid.uuid4().hex) + ".wav", format="wav")

    more = input("Keep going? ")
    
