import streamlit as st
from PIL import Image, ImageDraw
import base64

# Função para criar a imagem com bordas arredondadas (círculo perfeito)
def recorte_imagem_redonda(imagem_path):
    try:
        img = Image.open(imagem_path)
        largura, altura = img.size
        tamanho = min(largura, altura)
        img = img.crop(((largura - tamanho) // 2, (altura - tamanho) // 2, (largura + tamanho) // 2, (altura + tamanho) // 2))
        mask = Image.new('L', (tamanho, tamanho), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, tamanho, tamanho), fill=255)
        img.putalpha(mask)
        return img
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")
        return None

# Função para converter uma imagem para base64
def imagem_para_base64(caminho_imagem):
    with open(caminho_imagem, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Função principal
def main():
    # Adiciona a imagem de fundo ao menu lateral
    try:
        bg_image_base64 = imagem_para_base64("fotomenu.jpg")
        st.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] {{
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
        st.sidebar.error("Erro ao carregar a imagem de fundo do menu.")

    # Exibir imagem de perfil recortada no menu lateral
    img = recorte_imagem_redonda("portfolio.jpg")
    if img:
        st.sidebar.image(img, width=200)

    # Menu lateral de navegação
    st.sidebar.title("Menu de Navegação")
    menu = st.sidebar.radio("Escolha uma seção", ("Dados Pessoais", "Currículo", "Objetivo", "Formação", "Conhecimentos", "Experiência"))

    # Exibição de seções
    if menu == "Dados Pessoais":
        st.title("Dados Pessoais")
        st.write("""**Guilherme Henrique Damas dos Santos**  
        Idade: 24 anos  
        Nacionalidade: Brasileiro  
        Estado Civil: Solteiro  

        **Endereço**: Rua São José do Rio Preto, Parque Gramado II, Araraquara - SP  
        **Telefones**: (16) 99786-3751 / (16) 99628-4711  
        **E-mail**: [guisant1003@gmail.com](mailto:guisant1003@gmail.com)  
        **LinkedIn**: [Guilherme Henrique Damas dos Santos](https://linkedin.com/in/guilherme-henrique-damas-dos-santos-6b5543220)
        """)
    elif menu == "Currículo":
        st.title("Currículo Profissional")
        st.write("""**Engenheiro Civil** com experiência na execução e gerenciamento de projetos estruturais. Especializado em ferramentas como **Revit**, **Dynamo para Revit** e **Python** para automação de processos construtivos.""")
    elif menu == "Objetivo":
        st.title("Objetivo Profissional")
        st.write("""Buscar novas oportunidades no setor de **engenharia civil** com foco em **automação de processos** e **inovação**.""")
    elif menu == "Formação":
        st.title("Formação Acadêmica")
        st.write("""- **Dynamo para Revit** – **NeuroBIM** (Término Fev/2025)
        - **Programação em Python** – **SENAI** (2024)
        - **Pós-Graduação** em **Gestão de Projetos Sustentáveis de Edificações** – **Faculdade Alphaville** (2023)
        - **Graduação** em **Engenharia Civil** – **Universidade Paulista (UNIP)** (2022)
        - **Curso de AutoCAD (2D/3D)** – **UNIARA QUALIFICA** (2021)
        """)
    elif menu == "Conhecimentos":
        st.title("Conhecimentos e Habilidades")
        st.write("""- **Revit**: Modelagem e planejamento de projetos estruturais.
        - **Dynamo para Revit**: Criação de scripts para automação de tarefas.
        - **Python**: Desenvolvimento de scripts para cálculos estruturais e integração de dados.
        - **AutoCAD / STRAP / Ftool**: Detalhamento estrutural e cálculos.
        """)
    elif menu == "Experiência":
        st.title("Experiência Profissional")
        st.write("""**USICON Construções Pré-Fabricadas LTDA** (2020 – Atual)  
        - Modelagem paramétrica no **Revit** e desenvolvimento de rotinas no **Dynamo**.
        - Detalhamento de peças pré-fabricadas com **AutoCAD**, **Revit** e **Excel**.
        """)

# Executando o aplicativo
if __name__ == "__main__":
    main()
