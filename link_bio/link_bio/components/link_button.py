import reflex as rx

def link_button(text: str) -> rx.Component:
    return rx.button(
        text, 
        text_align = "center",
        height = "80px",
        width = "800px",
        radius = "large",
        background = rx.image(src = "/assets/images/TBM3_Avenger_-_Chino_Airshow_2014_(14344070442).jpg", width = "100%", height = "100%", object_fit = "cover"),
    )