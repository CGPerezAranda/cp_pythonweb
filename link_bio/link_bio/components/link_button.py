import reflex as rx

def link_button(text: str, url:str) -> rx.Component:
    return rx.link(
                rx.button(
                    text, 
                    text_align = "center",
                    height = "80px",
                    width = "800px",
                    radius = "large"
                ),
                href=url,
                is_external=1
    )