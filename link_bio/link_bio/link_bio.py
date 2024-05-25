import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links_maquetas import links_maquetas
from link_bio.views.links.links_teclados import links_teclados
from link_bio.components.separator import separator
from link_bio.components.footer import footer
import link_bio.styles.styles as styles


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
                margin_y = styles.Spacer.LARGE.value
                ),        
                footer(),
            align = "center",
            width = "100%",
            text_align = "center"
        )
    )

app = rx.App()
app.add_page(index)
 