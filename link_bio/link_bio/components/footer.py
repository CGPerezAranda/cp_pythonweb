import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.image (
            src="/giligingle.jpg", 
            width="300px",
            height="auto"),
        rx.vstack(
            rx.link(
                rx.image(
                    src="/github.jpg", 
                    width="100px",
                    height="auto",),
                    href="https://github.com/CGPerezAranda?tab=repositories"),
            rx.text("© 2024 - BC")
        )
    )