import reflex as rx
from link_bio.styles.styles import Size as Size
import link_bio.views.links.photo_links as photo_links


class CountState (rx.State):
    count: int = 1
    tbm3_link = photo_links.TBM3[count-1]

    def increment(self, max: int):
        if self.count == max:
            self.count = 1
            self.tbm3_link = photo_links.TBM3[self.count-1]
        else:
            self.count += 1
            self.tbm3_link = photo_links.TBM3[self.count-1]

    def decrement(self, max: int):
        if self.count == 1:
            self.count = max
            self.tbm3_link = photo_links.TBM3[self.count-1]
        else:
            self.count -= 1
            self.tbm3_link = photo_links.TBM3[self.count-1]
    
    @rx.var
    def index(self) -> int: 
        return 39

def giligingle() -> rx.Component: 
    max = 48
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
                    on_click=CountState.decrement(max),
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
                    on_click=CountState.increment(max),
                    width="3em",
                    position="sticky",
                ),
            ),
            rx.image(            
                    src=f"/images/Giligingles/giligingle ({CountState.count}).jpg",
                    width=Size.PHOTO.value,
                    height="auto",
                    align="center",
                                    
            ),
            align="center",
        )
    )

def photosTBM3() -> rx.Component:
    max = len(photo_links.TBM3)
    return rx.vstack(
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
                    on_click=CountState.decrement(max),
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
                    on_click=CountState.increment(max),
                    width="3em",
                    position="sticky",
                ),
            ),
            rx.image(    
                src=CountState.tbm3_link,
                width="100vh",
                height="auto",
                align="center",
            ),
            rx.box(
                rx.heading(f"CountState.count: {CountState.count}"),
            ),
            width="100vh",
            align="center",
        )
    