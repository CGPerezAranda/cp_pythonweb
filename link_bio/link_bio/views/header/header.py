import reflex as rx
from link_bio.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
                rx.vstack(
                    rx.avatar(
                        fallback="CP", 
                        size = "5", 
                        variant = "soft",
                        spacing = "2"),
                    rx.text("@CarlosPerez", size = "2"),
                ),
                rx.hstack(
                    link_icon("https://x.com/CGperezAr", "twitter"),
                    link_icon("https://www.instagram.com/cg.perezaranda/", "instagram"),
                    link_icon("https://www.linkedin.com/in/carlos-p%C3%A9rez-aranda-b157a834/", "linkedin")
                ),            
            align = "center",
        ),
        rx.text("""Mi nombre es Carlos. Me gustan las maquetas de plástico, especialmente de aviones, 
                    pasear por el campo con mi perra y mi mujer, los teclados mecánicos y la programación. 
                    Soy economista y estudiante de 4° curso de Ingeniería Informática .""", 
                    align = "left"),
        align = "center",
        width = "100%",
        text_align = "center"
        )