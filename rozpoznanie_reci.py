from speech_recognition import Recognizer, Microphone

zaznam = Recognizer()

def rozpoznanie():
            with Microphone() as zdroj_zvuku:
                print("Zacnite hovorit...")
                zvuk = zaznam.listen(zdroj_zvuku)
                try:
                    finalny_text = zaznam.recognize_google(zvuk, language="sk-SK")
                    print("Povedali ste: ", finalny_text)
                    if (finalny_text == "päť"):
                        print("Posielam signal - Pat [1, 1, 1, 1, 1]")

                    elif (finalny_text == "štyri"):
                        print("Posielam signal - Styri [1, 1, 1, 1, 0]")

                    elif (finalny_text == "tri"):
                        print("Posielam signal - Tri [0, 1, 1, 1, 0]")

                    elif (finalny_text == "dva"):
                        print("Posielam signal - Dva [0, 0, 1, 1, 0]")

                    elif (finalny_text == "jeden"):
                        print("Posielam signal - Jeden [0, 0, 0, 1, 0]")

                    elif (finalny_text == "jedna"):
                        print("Posielam signal - Jedna [0, 0, 0, 1, 0]")

                    else:
                        print("Zaznam - Nula [0, 0, 0, 0, 0]")
                except:
                     print("Nerozumiem reci tvojho kmena")

rozpoznanie()