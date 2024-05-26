import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
                rx.avatar(
                    fallback="CP", 
                    size = "5", 
                    variant = "soft",
                    spacing = "2"),
                rx.vstack(
                    rx.hstack(
                        link_icon("https://x.com/CGperezAr", "twitter"),
                        link_icon("https://www.instagram.com/cg.perezaranda/", "instagram"),
                        link_icon("https://www.linkedin.com/in/carlos-p%C3%A9rez-aranda-b157a834/", "linkedin"),
                    ),
                    rx.text(
                        "@CGPerezAr", 
                        weight = "bold",
                        font_size = Size.DEFAULT.value,
                        color = Text_colors.HEADER.value,
                    ),
                    
                    align = "start",
                ),            
            align = "center",
        ),
        rx.flex(
            info_text(
                "Deseando cambiar al sector IT", 
                "Desde el 2002 disfrutando en el sector financiero, desde el 2010 sufriéndolo.",
                ),
        ),
        rx.text(
            """Mi nombre es Carlos. Me gustan las maquetas de plástico, especialmente de aviones, 
            pasear por el campo con mi perra y mi mujer, los teclados mecánicos y la programación. 
            Soy economista, empleado de banca y estudiante de 4° curso de Ingeniería Informática.""", 
            align = "left",
            color = Text_colors.BODY.value,
            ),
        align = "center",
        width = "100%",
        text_align = "center"
        )