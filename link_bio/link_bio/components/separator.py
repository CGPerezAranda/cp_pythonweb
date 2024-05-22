import reflex as rx


def separator(text: str) -> rx.Component:
    return rx.center(
                rx.text(text),
                border_radius="15px",
                border_width="thick",
                width="100%",
            ),