import streamlit as st

st.title("Página principal.")

st.set_page_config(page_title="Dark Dev Portfolio", page_icon="🧛")

# --- DECORADOR ---
def style_section(func):
    """Adiciona uma linha divisória estética antes de cada seção"""
    def wrapper(*args, **kwargs):
        st.markdown("---")
        return func(*args, **kwargs)
    return wrapper

# --- SEÇÕES DA PÁGINA ---

@style_section
def intro():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Ritual dos programadores")
        st.write("""
        Bem-vindo ao Ritual dos programadores.
                 
        Aqui, códigos não são linhas. São ideias,experimentos, erros, madrugadas e criações.
                 
        Este espaço foi feito para desenvolvedores, curiosos e mentes criativas que desejam compartilhar projetos, conversas, aprender e evolir juntos.
                 
        Entre, deixe sua marca e faça parte da comunidade. O ritual apenas começou.""")
    with col2:
        st.metric(label="Status", value="Codando", delta="Sob efeito de Café")

        st.image("https://montessorimaispasque.com/wp-content/uploads/2020/01/photo-nosferatu-le-vampire-15.jpg")

@style_section
def galeria():
    st.header("Interesses & Projetos")
    # Grid simples de 3 colunas
    c1, c2, c3 = st.columns(3)
    c1.markdown("🦇 **Criaturas da noite**")
    c2.markdown("🎧 **Rock no fone**")
    c3.markdown("☕ **Café frio e ideias perigosas**")

@style_section
def contato():
    st.header("Contato")
    st.text_input("Deixe uma mensagem no vazio:")
    st.button("Enviar para a Escuridão")

# --- NAVEGAÇÃO E EXECUÇÃO ---

def main():
    # Barra de Navegação Horizontal usando Tabs (Sem HTML)
    tab_home, tab_about = st.tabs(["🌑 Home", "📖 Sobre"])

    with tab_home:
        intro()
        galeria()

    with tab_about:
        st.header("O Ritual de Programar")
        st.write("""
        Gosto de coisas melancólicas, livros antigos e música que preencha o quarto.
        Para mim, programar em Python é como desenhar: exige precisão, mas permite 
        uma liberdade criativa imensa.
        """)
        st.video("https://youtu.be/VK9b8nTl9Vo?list=RDVK9b8nTl9Vo")
        st.markdown("**⚰️Playlist Atual:** Helena(Three Cheers sweet Revenge) My Chemical Romance*")
        contato()

if __name__ == "__main__":
    main()