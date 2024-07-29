import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "Visita\assets\Actividades_fondo.jpg"

#Común
_meta=[
{"name": "og.type", "content": "website"},
{"name": "og.image", "content": preview}
]

#index

title_index="Resumen de los pacientes y actividades"
description_index="En esta página puedes visualizar un resumen de los pacientes y sus actividades clínicas asociadas, además de agrupaciones útiles de estos registros"
preview_index = "Visita/assets/Estación de Enfermería.jpg"

meta_index = [
    {"name": "og.title", "content": title_index},
    {"name": "og.description", "content": description_index}
]
meta_index.extend(_meta)

#Pacientes

title_pacientes="Para gestionar pacientes"
description_pacientes="En esta página puedes cargar, modificar, eliminar y consultar pacientes"
preview_pacientes = "Visita/assets/Imágen_Paciente.jpg"

meta_pacientes = [
    {"name": "og.title", "content": title_pacientes},
    {"name": "og.description", "content": description_pacientes}
]
meta_pacientes.extend(_meta)

#Actividades

title_actividades="Para gestionar actividades"
description_actividades="En esta página puedes cargar, modificar y eliminar actividades clínicas de la atención de pacientes"
preview_actividades = "Visita/assets/Imágen_Actividades.jpg"

meta_actividades = [
    {"name": "og.title", "content": title_actividades},
    {"name": "og.description", "content": description_actividades}
]
meta_actividades.extend(_meta)

