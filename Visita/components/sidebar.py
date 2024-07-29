import reflex as rx

def sidebar() -> rx.Component:
    return rx.hstack(
            rx.heading("", 
                       margin_bottom="1em",
                       text_decoration_line= "overline",
                       text_decoration_style="solid",
                       padding_top='15px'), 
            position="relative",
            height="100%",
            left="0px",
            top="0px",
            z_index="5",
            padding_x="2em",
            padding_y="2em",
            padding_right='7px',
            background_color="white",
            align_items="left",
            width="250px"
    )