import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.avatar(
                fallback="CP", 
                size = "5", 
                variant = "solid",
                spacing = "2"),
            rx.text("Hola mi nombre es Carlos Perez"),
            align = "center",
            width = "100%",
            text_align = "center"
        )