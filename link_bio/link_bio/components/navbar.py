import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Carlos Pérez",
            height = "40px",
            text_align = "center",         
        ),
        position="sticky",
        bg = "cyan",
        padding_x = "16px",
        padding_y = "8px", 
        z_index = "999"          
    )