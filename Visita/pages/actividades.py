import reflex as rx
from Visita.components.navbar import navbar
from Visita.components.Title import title
from Visita.Views.center import center
from Visita.components.footer import footer
from Visita.pages.routes import Route as Route
from Visita.pages import utils as utils
from Visita.Style import style


@rx.page(route= Route.ACTIVIDADES.value,
    title= utils.title_actividades,
    description= utils.description_actividades,
    #preview= utils.preview,
    meta=utils.meta_actividades
)

def actividades_ing() -> rx.Component:
       return rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                title("Actividades"),
                center(),
                width="100%"
            ),
            footer(),
max_width=style.MAX_WIDTH,
width="100%",
    )