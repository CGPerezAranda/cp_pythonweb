import reflex as rx
import link_bio.styles.styles as styles

def separator(text: str) -> rx.Component:
    return rx.heading(   
                rx.text(
                    text, 
                    size = styles.TextSize.DEFAULT.value
                    ),
                style =  styles.separator_style,    
    )