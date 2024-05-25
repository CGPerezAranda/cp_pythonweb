import reflex as rx
import random as rd


def footer() -> rx.Component:
    random_number = rd.randint(0, 25)
    return rx.hstack(
        rx.link(
            rx.image(
                src=f"/images/Giligingles/Giligingle ({random_number}).jpg",
                width="300px",
                height="auto"
            ),
            href = "https://imgur.com/a/0MMOu6E"
        ),
        rx.vstack(
            rx.link(
                rx.image(
                    src="/github.jpg", 
                    width="100px",
                    height="auto"
                ),
                href="https://github.com/CGPerezAranda?tab=repositories"
            ),
            rx.text("© 2024 - BC")
        )
    )
