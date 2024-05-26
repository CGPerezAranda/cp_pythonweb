import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors

def info_text(title: str, body: str)-> rx.Component:
    return rx.box(
        rx.text(
            title,
            color = Text_colors.HEADER.value,
            font_weight="bold",
            as_= "span",
        ),
        
        rx.text(
            rx.text.em(
                f" {body}",
                color = Text_colors.FOOTER.value,
                font_size = Size.DEFAULT.value,
                ),            
        )
    )