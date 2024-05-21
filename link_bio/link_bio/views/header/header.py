import reflex as rx

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.avatar(
                fallback="CP", 
                size = "5", 
                variant = "solid",
                spacing = "2"),
            rx.text("Hola mi nombre es Carlos Perez"),
            rx.center(
                rx.text("Hello World!"),
                border_radius="15px",
                border_width="thick",
                width="50%",
            )
            
        )
    )
