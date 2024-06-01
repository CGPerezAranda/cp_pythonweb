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
from link_bio.styles.colors import Color as color


class State(rx.State):
    pass

def index() -> rx.Component:

    return rx.center(
        rx.flex(
        navbar(), 
        rx.box(                                   
            rx.vstack(
                header(),
                separator("Mis maquetas"),
                links_maquetas(), 
                separator("Mis Teclados"),
                links_teclados(),
                max_width = styles.MAX_WIDTH,
                margin_y = styles.Size.LARGE.value,                
            ),   
            direction = "column", 
            margin = Size.LARGE.value,
            background = color.BACKGROUND.value,
            padding = Size.DEFAULT.value,
            border_radius = Size.SMALL.value,            
        ),
        footer(),
        background = "center/cover url('/background.jpg')",
        width="100%",
        height="100vh",
        z_index = "998",
        top = "0",
        direction = "column",
        align = "center",
        ),
    )
    
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style = styles.BASE_STYLE,
)
app.add_page(index)
app.add_page(giliginglesgalery, route = "/giliginglesgalery")
 