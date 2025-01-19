import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import base64

# Função para criar a imagem com bordas arredondadas (círculo perfeito)
def recorte_imagem_redonda(imagem_path):
    try:
        img = Image.open(imagem_path)

        # Garantindo que a imagem seja quadrada (tomando o menor lado)
        largura, altura = img.size
        tamanho = min(largura, altura)  # Pegamos o menor valor entre largura e altura para garantir o formato circular

        # Redimensionando a imagem para ser quadrada
        img = img.crop(((largura - tamanho) // 2, (altura - tamanho) // 2, (largura + tamanho) // 2, (altura + tamanho) // 2))

        # Criando uma máscara circular
        mask = Image.new('L', (tamanho, tamanho), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, tamanho, tamanho), fill=255)

        # Aplicando a máscara circular
        img.putalpha(mask)  # Colocando a máscara circular na imagem

        return img
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")
        return None

# Função para converter uma imagem para base64
def imagem_para_base64(caminho_imagem):
    try:
        with open(caminho_imagem, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception as e:
        st.error(f"Erro ao converter a imagem para base64: {e}")
        return None

# Função principal
def main():
    # Adiciona a imagem de fundo ao menu lateral
    try:
        bg_menu_base64 = imagem_para_base64("fotomenu.jpg")
        if bg_menu_base64:
            st.markdown(
                f"""
                <style>
                [data-testid="stSidebar"] {{
                    background-image: url("data:image/jpeg;base64,{bg_menu_base64}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.sidebar.error("Erro ao carregar a imagem de fundo do menu.")

    # Adiciona a imagem de fundo na tela principal
    try:
        bg_main_base64 = imagem_para_base64("fundoprincipal.jpg")
        if bg_main_base64:
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("data:image/jpeg;base64,{bg_main_base64}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error("Erro ao carregar a imagem de fundo principal.")

    # Exibe a imagem uma vez, na parte superior da barra lateral
    img = recorte_imagem_redonda("portfolio.jpg")  # Substitua com o caminho correto da imagem
    if img:
        st.sidebar.image(img, width=200)  # Exibe a imagem com recorte redondo na barra lateral no topo

    # Menu lateral para navegação
    st.sidebar.title("Menu de Navegação")
    menu = st.sidebar.radio("Escolha uma seção", ("Dados Pessoais", "Currículo", "Objetivo", "Formação", "Conhecimentos", "Experiência"))

    # Exibe a seção de acordo com a escolha do menu
    if menu == "Dados Pessoais":
        exibir_dados_pessoais()
    elif menu == "Currículo":
        exibir_curriculo()
    elif menu == "Objetivo":
        exibir_objetivo()
    elif menu == "Formação":
        exibir_formacao()
    elif menu == "Conhecimentos":
        exibir_conhecimentos()
    elif menu == "Experiência":
        exibir_experiencia()

# Outras funções (exibir_dados_pessoais, exibir_curriculo, etc.) permanecem as mesmas.

# Executando o aplicativo
if __name__ == "__main__":
    main()
