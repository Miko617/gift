import streamlit as st

st.set_page_config(page_title="Taylor's Version Mood", page_icon="🧣")

st.title("✨ Wybierz swoją Erę ✨")
st.write("Wybierz nastrój, a ja dobiorę odpowiedni soundtrack.")

eras = {
    "Energiczna / Do tańca": {
        "song": "Shake It Off",
        "lyric": "Cause the players gonna play, play, play...",
        "url": "https://www.youtube.com/watch?v=nfWlot6h_JM" 
    },
    "Sentymentalna / Spokojna": {
        "song": "Cardigan",
        "lyric": "And when I felt like I was an old cardigan under someone's bed...",
        "url": "https://www.youtube.com/watch?v=K-a8s8OLBSE"
    },
    "Pewna siebie / Boss lady": {
        "song": "The Man",
        "lyric": "I'd be a fearless leader, I'd be an alpha type.",
        "url": "https://www.youtube.com/watch?v=AqAJLh9wuZ0"
    },
    # Tu wpisałem nazwę dokładnie taką jak na Twoim screenshocie:
    "Nostalgiczna / Filmowa (Dla odważnych)": {
        "song": "Style",
        "lyric": "You got that James Dean daydream look in your eye...",
        "msg": "🎬 Skoro mamy już klimat, to może wybierzemy się do retro kina?",
        "url": "https://www.youtube.com/watch?v=-CmadmM5cOk"
    }
}

wybrany_nastroj = st.selectbox(
    "Jak się dzisiaj czujesz?",
    ["Wybierz opcję..."] + list(eras.keys())
)

if wybrany_nastroj != "Wybierz opcję...":
    dane = eras[wybrany_nastroj]
    
    st.divider()
    st.subheader(f"🎶 {dane['song']}")
    st.write(f"*\"{dane['lyric']}\"*")
    
    # POPRAWKA: Sprawdzamy po tytule piosenki - to zawsze zadziała!
    if dane['song'] == "Style":
        st.success(dane['msg'])
        st.balloons()
        
    st.video(dane['url'])
