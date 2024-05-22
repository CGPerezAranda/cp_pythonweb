import reflex as rx


def separator(text: str) -> rx.Component:
    return rx.center(
        
                rx.text(text),
                border_radius="15px",
                border_width="thick",
                width="100%",
                background_image= "https://upload.wikimedia.org/wikipedia/commons/d/d6/TBF_early1942.jpg"
            
    )