import reflex as rx
import random as rd
from link_bio.styles.styles import Size as size
from link_bio.styles.colors import Text_colors as text_colors
from link_bio.styles.colors import Color as color
from link_bio.styles.styles import IconSize as iconsize
import link_bio.styles.styles as styles
from link_bio.components.countstate import giligingle as giligingle


def footer() -> rx.Component:
    return rx.center(
            rx.hstack(
                rx.link(
                    rx.icon(
                        "github",
                        size=iconsize.MAX.value,
                        color = text_colors.HEADER.value,
                    ),
                    href="https://github.com/CGPerezAranda?tab=repositories",
                    is_external=1,
                ),
                rx.link(
                    rx.icon(
                        "gitlab",
                        size=iconsize.MAX.value,
                        color = text_colors.HEADER.value,
                        ),
                    href="https://gitlab.com/CGPerezAranda/python-web",
                    is_external=1,
                ),
                rx.icon(    
                    "creative-commons", 
                    size=iconsize.LARGE.value,
                    color = text_colors.HEADER.value,
                ),
                rx.icon(    
                    "copyright", 
                    size=iconsize.LARGE.value,
                    color = text_colors.HEADER.value,
                ),
                rx.text(
                    "2024 - CP",
                    font_size=size.MEDIUM.value,
                    font_family="Manrope",
                    color=text_colors.HEADER.value,
                ),  
            ),
        padding = size.DEFAULT.value,
        z_index = 1,
        margin_top = "auto",
        ),


