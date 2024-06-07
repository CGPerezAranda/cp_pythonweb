import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.countstate import photosTBM3 as photosTBM3
from link_bio.components.footer import footer
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors



def gallerytbm3() -> rx.Component:

    return rx.center(
        rx.flex(
            navbar(),
            rx.flex(
                rx.vstack(           
                    rx.box(
                        photosTBM3(),
                        margin=Size.MAX.value,
                        ),
                    ),  
                width="100%",
                direction="column",
                align = "center",
            ),
            footer(),
            direction="column",
            min_height="100vh",
            background = "center/cover url('/background.jpg')",
            width="100%",
        )
    )
        
    