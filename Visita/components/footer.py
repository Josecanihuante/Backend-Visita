import reflex as rx
from Visita.Style import style as style
from Visita.Style.style import Size as Size


def footer() -> rx.Component:
    return rx.hstack(
        rx.image(src="/Amor_data_science_App.jpg", width="250px", height="auto", alt="Logo del Desarrollador, Un corazón formado con grafos (relaciones de datos)"),
        #rx.icon('heart-handshake', width="3em", size=50, position= 'fixed', padding_top='1px', padding_right='1px', padding_left='5px', padding_bottom='5px', margin_left='260px', 
        #        color_scheme="gold"),
        rx.text('Data Science Hospital Padre Alberto Hurtado',
                color="gold", 
                margin_left= Size.SMALL.value, 
                margin_top=Size.LARGE.value
        ),
    z_index="777",
    position="Relative",
    margin_left=Size.SMALL.value,
    width="100%",
    height="100%",
    max_width= style.MAX_WIDTH,
    white_space= "normal"
    )