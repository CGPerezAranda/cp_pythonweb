import reflex as rx
from enum import Enum
from .colors import Color
from .colors import Text_colors

#constansts
MAX_WIDTH = "700px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Manrope&display=swap",
    "https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]

#Spacers
class Spacer(Enum):
    VSMALL = "0.3em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    LARGE = "2em"
    MAX = "4em"

#Sizes
class Size(Enum):
    ZERO = "0em"
    VVSMALL = "0.1em"
    VSMALL = "0.3em"
    SMALL = "0.5em"
    MEDIUM = "0.85em"
    DEFAULT = "1em"
    LARGE = "2em"
    MAX = "4em"
    PHOTO = "20em"

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
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%", 
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.DEFAULT.value,    
        "background_color": Color.CONTENT.value,
        "color": Text_colors.BODY.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
    },
    rx.heading: {
        "color": Text_colors.HEADER.value,
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

button_title_style = dict(
    size = Size.SMALL.value,
    color = Text_colors.HEADER.value,
)
button_body_style = dict(
    size = Size.VSMALL.value,
    color = Text_colors.BODY.value,
)

title_style = dict(
    font_size = TextSize.LARGE.value,
    color = Text_colors.HEADER.value,
)

separator_style = dict(
    width="100%",
    border_radius=Size.SMALL.value,
    border_width=Size.VVSMALL.value,  
    padding=Size.SMALL.value, 
    font_size = TextSize.LARGE.value,
)