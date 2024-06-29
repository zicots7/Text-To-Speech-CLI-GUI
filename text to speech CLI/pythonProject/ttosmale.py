import win32com.client as ws

def ml_():
    speaker_number = 0
    sr_ = ws.Dispatch("SAPI.SpVoice")
    vcs = sr_.GetVoices()
    sr_.Voice
    sr_.SetVoice(vcs.Item(speaker_number))
    sr_.Volume = 100
    sr_.Rate = -2
    while True:
       print("Enter what you want to speak ")
       s = input()
       sr_.Speak(s)
       if (s == 'exit'):
          sr_.Speak("Thanks for using ")
          break

