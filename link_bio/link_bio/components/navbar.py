import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import Text_colors as Text_colors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Carlos",
                color = Text_colors.IDENT1.value,
                as_ = "span",
            ),
            rx.text(
                "Pérez",
                color = Text_colors.IDENT2.value,
                as_ = "span",
            ),

        ),
        position="sticky",
        bg = Color.CONTENT.value,
        padding_x = Size.SMALL.value,
        padding_y = Size.SMALL.value, 
        z_index = "999",
        top = "0",
        width = "100%",     
    )