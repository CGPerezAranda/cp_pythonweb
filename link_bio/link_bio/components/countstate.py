import reflex as rx
from link_bio.styles.styles import Size as Size

class CountState (rx.State):
    count: int = 1

    def increment(self):
        if self.count == 26:
            self.count = 1
        else:
            self.count += 1

    def decrement(self):
        if self.count == 1:
            self.count = 26
        else:
            self.count -= 1

def giligingle(): 
    return rx.center(
        rx.vstack(
            rx.hstack( 
                rx.button(
                    rx.icon("arrow_left"),
                    border_radius="1em",
                    box_shadow="#245445 0 15px 30px -10px",
                    background_image="linear-gradient(144deg,#245445,#75ffd3)",
                    box_sizing="border-box",
                    color="white",
                    opacity=1,
                    _hover={
                        "opacity": 0.5,
                    },
                    on_click=CountState.decrement,
                    width="3em",
                    position="sticky",
                ),
                rx.button(
                    rx.icon("arrow_right"),
                    border_radius="1em",
                    box_shadow="#245445 0 15px 30px -10px",
                    background_image="linear-gradient(144deg,#245445,#75ffd3)",
                    box_sizing="border-box",
                    color="white",
                    opacity=1,
                    _hover={
                        "opacity": 0.5,
                    },
                on_click=CountState.decrement,
                width="3em",
                position="sticky",
                ),
            ),
            rx.image(
                    src=f"/images/Giligingles/Giligingle ({CountState.count}).jpg",
                    width=Size.PHOTO.value,
                    height="auto",
                    align="center",
            ),
            align="center",
        )
    )