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

# Função para aplicar CSS personalizado
def aplicar_css_personalizado(imagem_fundo):
    with open(imagem_fundo, "rb") as img_file:
        imagem_base64 = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
        /* Fundo da tela principal */
        .stApp {{
            background: url(data:image/png;base64,{imagem_base64});
            background-size: cover;
        }}

        /* Fundo da barra lateral */
        .css-1d391kg, .css-1d391kg nav {{
            background: url(data:image/png;base64,{imagem_base64});
            background-size: cover;
        }}

        /* Fundo da barra superior */
        header {{
            background: url(data:image/png;base64,{imagem_base64});
            background-size: cover;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Funções para exibir conteúdo
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

def exibir_curriculo():
    st.title("Currículo Profissional")
    st.header("Resumo das Qualificações")
    st.write("""
    **Engenheiro Civil** com forte experiência na execução e gerenciamento de projetos estruturais. 
    Especializado na utilização de ferramentas de ponta como **Revit**, **Dynamo para Revit** e **Python**, 
    que permitem otimizar o desenvolvimento de projetos e automação de processos construtivos. 
    """)

def exibir_objetivo():
    st.title("Objetivo Profissional")
    st.write("""
    Buscar novas oportunidades de **desenvolvimento e implementação de soluções tecnológicas** no setor de **engenharia civil**, 
    com foco em **automação de processos** e **inovação**.
    """)

def exibir_formacao():
    st.title("Formação Acadêmica")
    st.write("""
    - **Dynamo para Revit** – **NeuroBIM** (Término previsto Fev/2025)
    - **Programação em Python** – **SENAI** (2024)
    - **Pós-Graduação** em **Gestão de Projetos Sustentáveis de Edificações** – **Faculdade Alphaville** (2023)
    - **Graduação** em **Engenharia Civil** – **Universidade Paulista (UNIP)** (2022)
    - **Curso de AutoCAD (2D/3D)** – **UNIARA QUALIFICA** (2021)
    """)

def exibir_conhecimentos():
    st.title("Conhecimentos e Habilidades")
    st.write("""
    - **Revit**: Profundo domínio em **modelagem** e **planejamento** de projetos estruturais.
    - **Dynamo para Revit**: Criação de scripts para automação de tarefas.
    - **Python**: Desenvolvimento de **scripts** para automação de cálculos estruturais.
    - **AutoCAD / STRAP / Ftool**: Conhecimento avançado em **detalhamento estrutural** e **cálculos**.
    - **Idiomas**: Inglês básico (habilidade para leitura e compreensão de textos).
    """)

def exibir_experiencia():
    st.title("Experiência Profissional")
    st.markdown("""
    **USICON CONSTRUÇÕES PRÉ-FABRICADAS LTDA** (04/2022 – Atual)  
    - **Cargo**: Projetista Pleno  
      - Modelagem paramétrica no **Revit** e manutenção de projetos.
    """)

def main():
    aplicar_css_personalizado("fotomenu.jpg")

    img = recorte_imagem_redonda("portfolio.jpg")
    if img:
        st.sidebar.image(img, width=200)

    st.sidebar.title("Menu de Navegação")
    menu = st.sidebar.radio("Escolha uma seção", ("Dados Pessoais", "Currículo", "Objetivo", "Formação", "Conhecimentos", "Experiência"))

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

if __name__ == "__main__":
    main()
