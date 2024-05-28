import reflex as rx
import link_bio.styles.styles as styles

def separator(text: str) -> rx.Component:
    return rx.heading(   
                rx.text(
                    text, 
                    style = styles.title_style,
                    ),
                style =  styles.separator_style,    
    )