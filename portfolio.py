import streamlit as st
from PIL import Image, ImageDraw
import base64

# Função para criar a imagem com bordas arredondadas (círculo perfeito)
def recorte_imagem_redonda(imagem_path):
    try:
        img = Image.open(imagem_path)

        # Garantindo que a imagem seja quadrada (tomando o menor lado)
        largura, altura = img.size
        tamanho = min(largura, altura)

        # Redimensionando a imagem para ser quadrada
        img = img.crop(((largura - tamanho) // 2, (altura - tamanho) // 2, (largura + tamanho) // 2, (altura + tamanho) // 2))

        # Criando uma máscara circular
        mask = Image.new('L', (tamanho, tamanho), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, tamanho, tamanho), fill=255)

        # Aplicando a máscara circular
        img.putalpha(mask)

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
    # Adiciona a imagem de fundo à tela principal
    try:
        bg_image_base64 = imagem_para_base64("fundo_principal.jpg")  # Substitua com o caminho correto da imagem
        if bg_image_base64:
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("data:image/jpeg;base64,{bg_image_base64}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error("Erro ao carregar a imagem de fundo da tela principal.")

    # Adiciona a imagem de fundo ao menu lateral
    try:
        bg_sidebar_base64 = imagem_para_base64("fotomenu.jpg")
        if bg_sidebar_base64:
            st.markdown(
                f"""
                <style>
                [data-testid="stSidebar"] {{
                    background-image: url("data:image/jpeg;base64,{bg_sidebar_base64}");
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

    # Adiciona a imagem de fundo à barra superior
    try:
        top_bar_image_base64 = imagem_para_base64("barra_superior.jpg")  # Substitua pelo caminho correto da imagem
        if top_bar_image_base64:
            st.markdown(
                f"""
                <style>
                header {{ 
                    background-image: url("data:image/jpeg;base64,{top_bar_image_base64}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                    height: 80px; /* Ajuste a altura conforme necessário */
                }}
                header > div:first-child {{
                    display: none; /* Oculta o título padrão do Streamlit na barra superior */
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error("Erro ao carregar a imagem de fundo da barra superior.")

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

# Função para exibir os dados pessoais
def exibir_dados_pessoais():
    st.title("Dados Pessoais")
    st.write("""
    **Guilherme Henrique Damas dos Santos**  
    Idade: 24 anos  
    Nacionalidade: Brasileiro  
    Estado Civil: Solteiro  

    **Endereço**: Rua São José do Rio Preto, Parque Gramado II, Araraquara - SP  
    **Telefones**: (16) 99786-3751 / (16) 99628-4711  
    **E-mail**: [guisant1003@gmail.com](mailto:guisant1003@gmail.com)  
    **LinkedIn**: [Guilherme Henrique Damas dos Santos](https://linkedin.com/in/guilherme-henrique-damas-dos-santos-6b5543220)
    """)

# Função para exibir o currículo
def exibir_curriculo():
    st.title("Currículo Profissional")
    st.header("Resumo das Qualificações")
    st.write("""
    **Engenheiro Civil** com forte experiência na execução e gerenciamento de projetos estruturais.
    """)

# Função para exibir o objetivo
def exibir_objetivo():
    st.title("Objetivo Profissional")
    st.write("""
    Buscar novas oportunidades de desenvolvimento e implementação de soluções tecnológicas no setor de engenharia civil.
    """)

# Função para exibir a formação
def exibir_formacao():
    st.title("Formação Acadêmica")
    st.write("""
    - **Dynamo para Revit** – **NeuroBIM** (Término previsto Fev/2025)
    """)

# Função para exibir os conhecimentos
def exibir_conhecimentos():
    st.title("Conhecimentos e Habilidades")
    st.write("""
    - **Revit**: Profundo domínio em modelagem e planejamento de projetos estruturais.
    """)

# Função para exibir a experiência profissional
def exibir_experiencia():
    st.title("Experiência Profissional")
    st.markdown("""
    **USICON CONSTRUÇÕES PRÉ-FABRICADAS LTDA** (04/2022 – Atual)
    """)

# Executando o aplicativo
if __name__ == "__main__":
    main()
