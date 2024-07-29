import reflex as rx
from Visita.Style.style import Size as Size
from Visita.Style import style as style
from Visita.Style.colors import TextColor as TextColor

def title(text:str) -> rx.Component:
            return rx.blockquote(
                        text,
                        size="6",
                        margin_left= "210px",
                        margin_top="105px",
                        margin_bottom="0px",
                        weight= "medium"
                        )