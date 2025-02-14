import streamlit as st
import numpy as np

def predict_success(parity, af_volume, placenta):
    """Modello di previsione del successo della VCE basato sui coefficienti riportati nello studio."""
    
    # Coefficienti del modello (logit regression)
    intercept = 0.337
    coef_parity = 0.418  # Maggiore parità aumenta il successo
    coef_oligo = -1.26   # Oligoidramnios riduce il successo
    coef_posterior = 0.879 # Placenta posteriore aumenta il successo
    
    # Codifica delle variabili
    af_oligo = 1 if af_volume == "Oligoidramnios" else 0
    placenta_posterior = 1 if placenta == "Posteriore" else 0
    
    # Calcolo della probabilità di successo
    logit = intercept + (coef_parity * parity) + (coef_oligo * af_oligo) + (coef_posterior * placenta_posterior)
    probability = 1 / (1 + np.exp(-logit))  # Trasformazione logistica
    
    return probability * 100  # Percentuale

# Interfaccia Streamlit
st.title("Calcolatore di Successo della Versione Cefalica Esterna (VCE)")
st.write("Inserisci le seguenti informazioni per stimare la probabilità di successo della procedura.")

# Input utente
parity = st.number_input("Numero di gravidanze a termine (parità)", min_value=0, max_value=10, value=1)
af_volume = st.selectbox("Volume del liquido amniotico", ["Normale", "Oligoidramnios", "Polidramnios"])
placenta = st.selectbox("Posizione della placenta", ["Anteriore", "Posteriore", "Laterale/Fundica"])

# Calcolo del punteggio
if st.button("Calcola Probabilità di Successo"):
    success_prob = predict_success(parity, af_volume, placenta)
    st.write(f"### Probabilità di successo della VCE: {success_prob:.1f}%")
