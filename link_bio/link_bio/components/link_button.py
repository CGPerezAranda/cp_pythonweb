import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body:str, url:str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(
                            "arrow-right", 
                            size = styles.IconSize.MAX.value,
                            ),
                        rx.vstack(
                            rx.text(title, size = styles.TextSize.DEFAULT.value),
                            rx.text(body, size = styles.TextSize.SMALL.value),
                            align = "start"
                        ),
                        align="center",
                    ),
                ),
                width="100%",
                href=url,
                is_external=1,
    )