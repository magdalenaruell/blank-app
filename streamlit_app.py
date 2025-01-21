import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Definition der Pflegebereiche mit Anforderungen
pflegebereiche = {
    "2.01": "Allgemeine Pflege",
    "2.02": "Neugeborenenstation",
    "2.03": "Intensivstation",
    "2.04": "Geriatrie",
    "2.05": "Isolierstation"
}

# Szenario-Funktionen
def ersatz_fuer_neugeborenenstation():
    return ["Intensivstation"]

def kombinierbare_stationen():
    return [("Allgemeine Pflege", "Geriatrie"), ("Intensivstation", "Isolierstation")]

def interimsnutzung_pandemie():
    return ["Intensivstation", "Isolierstation"]

def temporaere_unterbringung():
    return {bereich: "Alternativen prüfen" for bereich in pflegebereiche.values()}

# Streamlit GUI
st.title("Pflegebereichs-Planung")

option = st.selectbox("Wähle ein Szenario:", [
    "Ersatz für Neugeborenenstation",
    "Kombinierbare Stationen",
    "Interimsnutzung bei Pandemie",
    "Temporäre Unterbringung bei Umbau"
])

if st.button("Lösung anzeigen"):
    if option == "Ersatz für Neugeborenenstation":
        st.write(ersatz_fuer_neugeborenenstation())
    elif option == "Kombinierbare Stationen":
        st.write(kombinierbare_stationen())
    elif option == "Interimsnutzung bei Pandemie":
        st.write(interimsnutzung_pandemie())
    elif option == "Temporäre Unterbringung bei Umbau":
        st.write(temporaere_unterbringung())
