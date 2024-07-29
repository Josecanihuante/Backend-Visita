import reflex as rx
from Visita.Style import style as style
from Visita.Style.style import Size as Size
from Visita.Style.colors import Color as Color
from Visita.Style.colors import TextColor as TextColor
from Visita.pages.routes import Route as Route

def navbar() -> rx.Component:
    return rx.hstack(
            rx.icon('dna', width="3em", size=50, position= "fixed", padding_top="1px", padding_right="1px", padding_left="5px", padding_bottom="5px", margin_lef="15px", alt="Logo de la App. Cadena de ADN", color_scheme="black"),
            rx.link(
            rx.heading("Redmine", 
                    margin_bottom="1em",
                    text_decoration_line= "overline",
                    text_decoration_style="solid",
                    text_decoration_thickness="auto",
                    padding_left='60px',
                    padding_top='10px',
                    margin_right='10px',
                    color=TextColor.HEADER.value,
                    ),
                    href=Route.INDEX.value,
                    _hover = {"color":"cyan"}
                    ),
            rx.link(
                 rx.blockquote("Resumen", font_size= '19px', margin_left = Size.SMALL.value), 
                        weight= "medium",
                        color= TextColor.BODY.value,
                        margin_top= Size.SMALL.value,
                        href=Route.INDEX.value,
                        _hover={"color":"cyan"}
                        ),
            rx.link(
                rx.blockquote("Pacientes", font_size= '19px', margin_left = Size.SMALL.value), 
                        weight= "medium",
                        color= TextColor.BODY.value,
                        margin_top= Size.SMALL.value,
                        href=Route.PACIENTES.value,
                        _hover={"color":"cyan"} 
                        ),
            rx.link(
                rx.blockquote("Actividades", font_size= '19px', margin_left = Size.SMALL.value), 
                        weight= "medium",
                        color= TextColor.BODY.value,
                        margin_top= Size.SMALL.value,
                        href=Route.ACTIVIDADES.value,
                        _hover={"color":"cyan"} 
                        ),
            position="relative",
            height="100%",
            left="0px",
            top="0px",
            padding_x="1em",
            padding_y="1em",
            margin_bottom='0px',
            background_color="transparent",
            align_items="left",
            max_width= style.MAX_WIDTH,
            style= style.navbar_title_style,
            z_index="666"
)