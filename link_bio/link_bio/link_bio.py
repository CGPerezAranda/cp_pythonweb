import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links_maquetas import links_maquetas
from link_bio.views.links.links_teclados import links_teclados
from link_bio.components.separator import separator
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.components.giliginglesgalery import giliginglesgalery


class State(rx.State):
    pass

def index() -> rx.Component:

    return rx.center(
        rx.vstack(
            navbar(),        
            rx.vstack(
                header(),
                separator("Mis maquetas"),
                links_maquetas(), 
                separator("Mis Teclados"),
                links_teclados(),
                max_width = styles.MAX_WIDTH,
                margin_y = styles.Size.LARGE.value
                ),        
                footer(),
            align = "center",
            text_align = "center",
            width = "100%",
        )
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style = styles.BASE_STYLE,
)
app.add_page(index)
app.add_page(giliginglesgalery, route = "/giliginglesgalery")
 