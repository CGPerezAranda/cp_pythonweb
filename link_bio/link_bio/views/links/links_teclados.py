import reflex as rx
from link_bio.components.link_button import link_button

def links_teclados() -> rx.Component:
    return rx.vstack(
        link_button("Proyectos antiguos" ,"https://imgur.com/a/Kqphpq3"),
        align = "center",
        width = "100%",
        text_align = "center"
    )
    