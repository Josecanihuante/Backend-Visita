import reflex as rx
from Visita.Style import style
from Visita.pages.index import index as index
from Visita.pages.pacientes import pacientes_ing as pacientes
from Visita.pages.actividades import actividades_ing as actividades
from Visita.pages import utils as utils

class State(rx.State):
    "pass"

app = rx.App(
    stylesheets=style.STYLESHEETS,
    style= style.BASE_STYLE,
    head_components= [
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id=G-5S4G6E0CTQ"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-5S4G6E0CTQ');
"""
        ),
    ],
)
title = "Software de Gestión de Visitas y Optimización del Proceso de Atención Clínica"
descripcion = "Este Software permite registrar los pacientes y las instancias de atención a efectos de reducir los nudos críticos de su proceso clínico"
preview = "Visita\assets\Actividades_fondo.jpg"



app.add_page(index,
title = title,
description=descripcion,
image= "Amor_data_science_App.jpg", 
meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": title},
    {"name": "og:description", "content": descripcion},
    {"name": "og:preview", "content": preview},

]
)
app.add_page(pacientes)
app.add_page(actividades)