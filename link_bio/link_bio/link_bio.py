import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.separator import separator

class State(rx.State):
    pass

def index() -> rx.Component:

    return rx.center(
        rx.vstack(
            navbar(),        
            rx.vstack(
                header(),
                separator("Mis maquetas"),
                links(), 
                max_width = "800px",
                    width = "80%",
                ),        
            align = "center",
            width = "100%",
            text_align = "center"
        )
    )

app = rx.App()
app.add_page(index)
app._compile()   