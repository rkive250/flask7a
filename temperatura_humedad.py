import flet as ft
import requests

URL_SERVIDOR_FLASK = "https://flask7a-4m4l.onrender.com/"

def obtener_datos(filtro=None):
    try:
        response = requests.get(f"{URL_SERVIDOR_FLASK}/buscar", params={'filtro': filtro or ''})
        response.raise_for_status()  
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return []

def insertar_dato(telefono, nombre_curso):
    try:
        response = requests.post(
            f"{URL_SERVIDOR_FLASK}/alumnos/guardar", 
            data={'tel': telefono, 'ncurso': nombre_curso}
        )
        response.raise_for_status() 
        return response.json().get('message', '')
    except requests.exceptions.RequestException as e:
        print(f"Error al insertar el curso: {e}")
        return str(e)

def eliminar_dato(id_curso):
    try:
        response = requests.delete(f"{URL_SERVIDOR_FLASK}/alumnos/eliminar/{id_curso}")
        response.raise_for_status()  
        return response.json().get('message', '')
    except requests.exceptions.RequestException as e:
        print(f"Error al eliminar el curso: {e}")
        return str(e)

def main(page: ft.Page):
    page.title = "Gestión de Cursos"
    page.vertical_alignment = ft.MainAxisAlignment.START

    tabla_datos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Nombre del Curso")),
            ft.DataColumn(ft.Text("ID del Curso")),
            ft.DataColumn(ft.Text("Acciones")),
        ]
    )

    def visualizar_datos(filtro=None):
        datos = obtener_datos(filtro)
        tabla_datos.rows.clear()  

        for registro in datos:
            telefono, nombre_curso, id_curso = registro[1], registro[2], registro[0]
            eliminar_btn = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=id_curso: eliminar_click(e, id),
                tooltip="Eliminar"
            )
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(telefono)),
                    ft.DataCell(ft.Text(nombre_curso)),
                    ft.DataCell(ft.Text(str(id_curso))),
                    ft.DataCell(eliminar_btn),
                ]
            )
            tabla_datos.rows.append(fila)
        page.update()

    def insertar_click(event):
        telefono = txt_telefono.value
        nombre_curso = txt_nombre_curso.value
        if telefono and nombre_curso:
            mensaje = insertar_dato(telefono, nombre_curso)
            if "guardados correctamente" in mensaje:
                page.add(ft.AlertDialog(
                    title="Inserción exitosa", 
                    content=ft.Text(mensaje)
                ))
                visualizar_datos()  
            else:
                page.add(ft.AlertDialog(
                    title="Error al insertar", 
                    content=ft.Text(mensaje)
                ))
        else:
            page.add(ft.AlertDialog(
                title="Error de entrada", 
                content=ft.Text("Por favor, ingrese todos los campos.")
            ))

    def eliminar_click(event, id_curso):
        mensaje = eliminar_dato(id_curso)
        if "eliminado correctamente" in mensaje:
            page.add(ft.AlertDialog(
                title="Eliminación exitosa", 
                content=ft.Text(mensaje)
            ))
            visualizar_datos()  
        else:
            page.add(ft.AlertDialog(
                title="Error al eliminar", 
                content=ft.Text(mensaje)
            ))

    def buscar_click(event):
        filtro = txt_buscar.value
        visualizar_datos(filtro)  

    txt_telefono = ft.TextField(label="Teléfono", autofocus=True, width=300)
    txt_nombre_curso = ft.TextField(label="Nombre del Curso", width=300)
    btn_insertar = ft.ElevatedButton("Insertar", on_click=insertar_click)
    
    txt_buscar = ft.TextField(label="Buscar por nombre del curso", on_change=buscar_click)

    page.add(txt_telefono, txt_nombre_curso, btn_insertar, txt_buscar, tabla_datos)

    visualizar_datos()

ft.app(target=main)
