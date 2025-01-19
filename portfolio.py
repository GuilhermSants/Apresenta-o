import streamlit as st
from PIL import Image, ImageDraw, ImageOps

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

# Funções para exibir conteúdos
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

# Outras funções permanecem iguais...
# Adicionar funções exibir_curriculo(), exibir_objetivo(), exibir_formacao(), exibir_conhecimentos(), exibir_experiencia() aqui

# Função principal
def main():
    # Carregar a imagem de fundo do menu
    try:
        menu_bg = Image.open("fotomenu.jpg")
    except Exception as e:
        st.sidebar.error("Erro ao carregar a imagem de fundo do menu.")
        menu_bg = None

    # Exibir a imagem do usuário no menu (recortada em círculo)
    img = recorte_imagem_redonda("portfolio.jpg")
    if img:
        st.sidebar.image(img, width=200)

    # Menu lateral com imagem de fundo
    if menu_bg:
        st.sidebar.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] {{
                background-image: url("data:image/jpeg;base64,{menu_bg.tobytes().hex()}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Exibição do menu
    st.sidebar.title("Menu de Navegação")
    menu = st.sidebar.radio("Escolha uma seção", ("Dados Pessoais", "Currículo", "Objetivo", "Formação", "Conhecimentos", "Experiência"))

    # Exibe a seção correspondente
    if menu == "Dados Pessoais":
        exibir_dados_pessoais()
    # Inserir chamadas para as outras funções (exibir_curriculo, exibir_objetivo, etc.)

# Executando o aplicativo
if __name__ == "__main__":
    main()
