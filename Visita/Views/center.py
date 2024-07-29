import reflex as rx
from Visita.Style.style import Size as Size
from Visita.Style.colors import TextColor as TextColor
from Visita.Style.font import Font as Font
from Visita.Style.font import FontWeight as FontWeight

def center() -> rx.Component:
    return rx.center(
                rx.vstack(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Incidentes"),
                                rx.table.column_header_cell("Abiertas"),
                                rx.table.column_header_cell("Cerradas"),
                                rx.table.column_header_cell("Totales")
                            ),
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.row_header_cell("Actividades",
                                                        color=TextColor.HEADER.value),
                                rx.table.cell("110",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("380",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("490",
                                            color= TextColor.BODY.value,
                                            text_align="center")
                            ),
                            rx.table.row(
                                rx.table.row_header_cell("Pacientes",
                                                        color=TextColor.HEADER.value),
                                rx.table.cell("140",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("394",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("434",
                                            color= TextColor.BODY.value,
                                            text_align="center")
                            ),
                            rx.table.row(
                                rx.table.row_header_cell("Programadas",
                                                        color=TextColor.HEADER.value),
                                rx.table.cell("0",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("0",
                                            color= TextColor.BODY.value,
                                            text_align="center"),
                                rx.table.cell("0",
                                            color= TextColor.BODY.value,
                                            text_align="center")
                            ),
                        ),
                        variant='surface',
                        size='3',
                        align= 'center',
                        z_index="888",
                        white_space="normal",
                        alt="Tabla con la cantidad de pacientes y actividades disponibles en la Base de Datos"
                        ),
                        margin_bottom= '210px',
                        position="relative",
                        margin_left='210px'
                        )
    )
