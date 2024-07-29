import reflex as rx
from Visita.components.navbar import navbar
from Visita.components.Title import title
from Visita.Views.center import center
from Visita.components.footer import footer
from Visita.pages.routes import Route as Route
from Visita.pages import utils as utils
from Visita.Style import style

@rx.page(route= Route.INDEX.value,
    title= utils.title_index,
    description= utils.description_index,
    meta=utils.meta_index
)

def index() -> rx.Component:
       return rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                title("Resumen"),
                center(),
                width="100%"
            ),
            footer(),
max_width=style.MAX_WIDTH,
width="100%",
    )