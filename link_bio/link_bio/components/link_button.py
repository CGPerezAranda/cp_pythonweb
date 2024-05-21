import reflex as rx

def link_button(text: str) -> rx.Component:
    return rx.button(text, text_align = "center")