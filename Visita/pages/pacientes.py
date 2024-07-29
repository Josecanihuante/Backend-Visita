import reflex as rx
from Visita.components.navbar import navbar
from Visita.components.Title import title
from Visita.Views.center import center
from Visita.components.footer import footer
from Visita.pages.routes import Route as Route
from Visita.pages import utils as utils
from Visita.Style import style


@rx.page(route= Route.PACIENTES.value,
    title= utils.title_pacientes,
    description= utils.description_pacientes,
    #preview= utils.preview,
    meta=utils.meta_pacientes
)

def pacientes_ing() -> rx.Component:
       return rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                title("Pacientes"),
                center(),
                width="100%"
            ),
            footer(),
max_width=style.MAX_WIDTH,
width="100%",
    )