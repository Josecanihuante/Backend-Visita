import reflex as rx
from enum import Enum
from Visita.Style.colors import Color as Color
from Visita.Style.font import Font as Font
from Visita.Style.font import FontWeight as FontWeight

MAX_WIDTH='1600px' 


STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300;500&display=swap"
]   


class Size(Enum):
    ZERO = "0PX !important"
    SMALL ="10px"
    MEDIUM = "20px"
    DEFAULT = "42px"
    LARGE = "105px"
    BIG = "210px"

BASE_STYLE={
    "background": "linear-gradient(cyan, blue)",
    "background_size": "100%",
    "background_attachment": "fixed",
    "background_repeat": "no-repeat",
    "background_position": "center",
    "overflow": "auto",
    "white_space": "normal",
    "width":"100%",
    "height":"100%",

    "table":{
        "width":"100%",
        "height":"100%",
        "text_align": "start",
        "margin_bottom": "'105px",
        "marging_right": Size.DEFAULT.value,
        "white_space": "normal",
        "font_family": Font.HEADER.value,
        "font_weight": FontWeight.LIGHT.value,
        "background_color": "transparent"
}, 
    "th":{"padding": "15px",
        "font_family": Font.HEADER.value,
        "font_weight": FontWeight.LIGHT.value,
        "text_align": "start"},
        "white_space": "normal",
    "heading":{
        "margin_top": "105px",
        "white_space": "normal",
        "background_color": "transparent",
        "font_family": Font.HEADER.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    "icon":{
        "background_color": "transparent"
    }
    }

navbar_title_style = dict(
    font_family = Font.HEADER.value,
    font_weight= FontWeight.MEDIUM.value
)

blockquote_title_style = dict(
    font_family = Font.HEADER.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size = "20px"
)

footer_style = dict(
    font_family = Font.HEADER.value,
    font_weight= FontWeight.MEDIUM.value
)

