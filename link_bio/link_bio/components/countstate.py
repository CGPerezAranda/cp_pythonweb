import reflex as rx
from link_bio.styles.styles import Size as Size

class CountState (rx.State):
    count: int = 1

    def increment(self):
        if self.count == 26:
            self.count = 1
        else:
            self.count += 1

def giligingle(): 
    return rx.vstack( 
        rx.image(
            src=f"/images/Giligingles/Giligingle ({CountState.count}).jpg",
            width=Size.PHOTO.value,
            height="auto"
        ),
        rx.button(
            "Siguiente Giligingle",
            border_radius="1em",
            box_shadow="#245445 0 15px 30px -10px",
            background_image="linear-gradient(144deg,#245445,#75ffd3)",
            box_sizing="border-box",
            color="white",
            opacity=1,
            _hover={
                "opacity": 0.5,
            },
            on_click=CountState.increment,
            width="10em",
        ),
        align="center",
        width="100%",
    )