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
                            rx.text(
                                title, 
                                size = styles.TextSize.DEFAULT.value,
                                style = styles.button_title_style,
                                ),
                            rx.text(
                                body, 
                                size = styles.TextSize.SMALL.value,
                                style = styles.button_body_style,
                                ),
                            align = "start",
                            spacing="0",
                        ),
                        align="center",
                        height="100%",
                    ),
                ),
                height = styles.ButtonHeight.DEFAULT.value,
                width="100%",
                href=url,
                is_external=1,
    )