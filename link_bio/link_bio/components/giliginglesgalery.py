import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.countstate import giligingle as giligingle
from link_bio.components.navbar import navbar

def giliginglesgalery() -> rx.Component:

    return rx.center(
        rx.vstack(
            navbar(),
            rx.box(
                rx.text("Giligingles Galery"),
                giligingle(),
                width="100%",
                margin="1em",
            ),
            width="100%",
        ),
    )