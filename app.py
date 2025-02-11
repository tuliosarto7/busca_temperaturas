import streamlit as st
import requests


key = "229c8ef774ad9a9b4ca5a10c6b98430c"

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="center-content">', unsafe_allow_html=True)
cidade = st.text_input("Digite o nome da cidade:")
st.markdown('</div>', unsafe_allow_html=True)






campo_valores = st.empty()

if cidade:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric"
    
    resposta = requests.get(url)

    if resposta.status_code == 200:  
        dados = resposta.json()  
        temperatura = int(dados["main"]["temp"])  
        icon_tempo = dados["weather"][0]["icon"]  
        sensacao_termica = int(dados["main"]["feels_like"])

        cidade_formatada = cidade.capitalize()

        
        url_png = f"https://openweathermap.org/img/wn/{icon_tempo}@2x.png"

    
        st.markdown(f"""
            <div class="center-content">
                <img src="{url_png}" alt="Imagem tempo"> 
                <h5>A temperatura atual de {cidade_formatada} é {temperatura}°C</h5> 
                <p><strong>Sensação térmica: {sensacao_termica}°C</p>


            </div>

        """, unsafe_allow_html=True)

        
        #st.text(dados)
    elif resposta.status_code == 404: 
        st.text("Cidade não encontrada.")
    else:
        st.text("Erro na requisição")
