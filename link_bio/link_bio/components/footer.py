import reflex as rx
import random as rd
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors
import link_bio.styles.styles as styles


def footer() -> rx.Component:
    random_number = rd.randint(1, 26)
    return rx.vstack(
        rx.link(
            rx.image(
                src=f"/images/Giligingles/Giligingle ({random_number}).jpg",
                width = Size.PHOTO.value,
                height="auto"
            ),
            href = "https://imgur.com/a/0MMOu6E",
            is_external=1
            
        ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="/github.jpg", 
                    width="100px",
                    height="auto"
                ),
                href="https://github.com/CGPerezAranda?tab=repositories",
                is_external=1
            ),
            rx.link(
                rx.image(
                    src="/gitlab.png", 
                    width="100px",
                    height="auto"
                ),
                href = "https://gitlab.com/CGPerezAranda/python-web",
                is_external=1
            ),
            rx.vstack(
                rx.text(
                    "© 2024 - BC",
                    font_size = Size.MEDIUM.value,
                    color = Text_colors.FOOTER.value,
                ),
            ),            
            align = "center",
        ),
        margin_bottom = Size.LARGE.value,
        align = "center",
        width = "100%",
    )
    
