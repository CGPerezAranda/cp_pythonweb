import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.countstate import photos as photos
from link_bio.components.footer import footer
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_colors as Text_colors
from link_bio.components.countstate import CountState as CountState

def gallerytbm3() -> rx.Component:
    
    subject = "TBM3"
    CountState.setSubject(subject)

    return rx.center(
        rx.flex(
            navbar(),
            rx.flex(
                rx.vstack(           
                    rx.box(
                        photos(),
                        margin=Size.DEFAULT.value,
                        width="100%",
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
        
    