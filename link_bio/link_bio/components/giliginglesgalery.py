import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.countstate import giligingle as giligingle
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors


def giliginglesgalery() -> rx.Component:

    return rx.center(
        rx.flex(
            navbar(),
            rx.vstack(           
                rx.box(
                    giligingle(),
                    width="100%",
                    margin=Size.MAX.value,
                    ),
                ),
            footer(),
            background = "center/cover url('/background.jpg')",
            width="100%",
            height="100%",
            position="fixed",
            z_index = "998",
            top = "0",
            direction = "column",
            align = "center",
        ),
    )
        
    