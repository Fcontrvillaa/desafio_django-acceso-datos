from .models import Tarea, SubTarea


def imprimir_en_pantalla():
    tareas = Tarea.objects.all()
    

    for t in tareas:
        print(f"El id de tarea es:{t.id} descripcion: {t.descripcion}, estado:{t.eliminada}")
        if hasattr(t, "subtarea"):
            for s in t.subtarea.all().order_by("id"):

                print(f"El id es: {s.id} subtarear.{s.descripcion}")
    

def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)

    tarea.save()
    imprimir_en_pantalla()
    

def borrar_tarea(id):
    tarea = Tarea.objects.filter(id=id)

    tarea.delete()
    imprimir_en_pantalla()

def crear_sub_tarea(tarea, descripcion_subtarea):
    tarea_id= Tarea.objects.get(id=tarea)
    sub_tarea = SubTarea(tarea_id=tarea_id, descripcion=descripcion_subtarea)

    sub_tarea.save()
    return sub_tarea


def borrar_sub_tarea(sub_tarea_id):
    sub_tarea = SubTarea.objects.filter(id=sub_tarea_id)

    sub_tarea.delete()
    imprimir_en_pantalla()
    