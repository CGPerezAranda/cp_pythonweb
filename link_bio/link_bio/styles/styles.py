import reflex as rx
from enum import Enum

#constansts
MAX_WIDTH = "600px"

#Spacers
class Spacer(Enum):
    VSMALL = "0.3em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    LARGE = "2em"
    MAX = "4em"

#Sizes
class Size(Enum):
    VVSMALL = "0.1em"
    VSMALL = "0.3em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    LARGE = "2em"
    MAX = "4em"

class IconSize(Enum):
    SMALL = 15
    DEFAULT = 20
    LARGE = 25
    MAX = 30

class TextSize(Enum):
    VSMALL = "1"
    SMALL = "2"
    DEFAULT = "3"
    LARGE = "5"
    MAX = "7"

class ButtonWidth(Enum):
    SMALL = "20em"
    DEFAULT = "40em"
    LARGE = "60em"
    MAX = "80em"

class ButtonHeight(Enum):
    SMALL = "2em"
    DEFAULT = "3em"
    LARGE = "4em"
    MAX = "5em"

#Styles

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%", 
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value,    
    },
    rx.center: {
        "width": "100%",
        "height": "100%",       
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    },
    rx.hstack: {
        "align": "center",
    }
}

button_tittle_style = dict(
    size = Size.SMALL.value,
)
button_body_style = dict(
    size = Size.VSMALL.value,
)

separator_style = dict(
    width="100%",
    border_radius=Size.SMALL.value,
    border_width=Size.VVSMALL.value,  
    padding=Size.SMALL.value, 
)