import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.avatar(
                fallback="BC", 
                size = "5", 
                variant = "soft",
                spacing = "2"),
            rx.text("Bienvenido a la página de mis proyectos, unos acabados y otros en proceso."),
            align = "center",
            width = "100%",
            text_align = "center"
        )