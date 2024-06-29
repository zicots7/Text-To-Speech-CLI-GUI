import win32com.client as ws


def func():
    speaker_number = 0
    spkr = ws.Dispatch("SAPI.SpVoice")
    vcs = spkr.GetVoices()
    spkr.Voice
    spkr.SetVoice(vcs.Item(speaker_number))
    spkr.Volume = 100
    spkr.Rate = -2
    while True:
        print("Enter what you want to speak ")
        s = input()
        spkr.Speak(s)
        if s == 'exit':
            spkr.Speak("Thanks for using ")
            break


func()
