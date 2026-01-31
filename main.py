import time

def taylor_swift_mood_selector():
    # Baza danych nastrojów i piosenek
    eras = {
        "1": {
            "mood": "Energiczna / Do tańca",
            "song": "Shake It Off",
            "lyric": "Cause the players gonna play, play, play..."
        },
        "2": {
            "mood": "Sentymentalna / Spokojna",
            "song": "Cardigan",
            "lyric": "And when I felt like I was an old cardigan under someone's bed..."
        },
        "3": {
            "mood": "Pewna siebie / Boss lady",
            "song": "The Man",
            "lyric": "I'd be a fearless leader, I'd be an alpha type."
        },
        # ZMODYFIKOWANA OPCJA DLA ODWAŻNYCH (Retro Kino)
        "4": {
            "mood": "Nostalgiczna / Filmowa (Retro Vibe)",
            "song": "Style (Cinema Version)",
            "lyric": "You got that James Dean daydream look in your eye... A może sprawdzimy ten klimat w starym kinie?"
        }
    }

    print("✨ Witaj w generatorze nastroju Taylor Swift! ✨")
    print("------------------------------------------------")
    time.sleep(1) 
    
    print("Jak się dzisiaj czujesz? Wybierz numer:")
    
    for key, value in eras.items():
        print(f"[{key}] - {value['mood']}")

    print("------------------------------------------------")
    
    wybor = input("Twój wybór (wpisz numer): ")

    print("\nSzukam odpowiedniej ścieżki dźwiękowej...\n")
    time.sleep(2) 

    if wybor in eras:
        wybrana_era = eras[wybor]
        print(f"🎶 Piosenka dla Ciebie: {wybrana_era['song']}")
        print(f"💬 Przekaz dnia: \"{wybrana_era['lyric']}\"")
        
        if wybor == "4":
            print("\n🎬 (Biletów jeszcze nie mam, ale repertuar możemy wybrać razem!)")
    else:
        print("Taylor jeszcze o tym nie zaśpiewała. Spróbuj wybrać inny numer!")

if __name__ == "__main__":
    taylor_swift_mood_selector()