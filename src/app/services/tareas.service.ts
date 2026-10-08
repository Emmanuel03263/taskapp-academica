import { Injectable, signal } from '@angular/core';

import { PrioridadTarea, Tarea } from '../models/tarea.model';

const STORAGE_KEY = 'taskapp-academica-tareas-v2';

@Injectable({
  providedIn: 'root'
})
export class TareasService {
  private readonly tareasSignal = signal<Tarea[]>(this.cargarTareas());

  readonly tareas = this.tareasSignal.asReadonly();

  agregarTarea(datos: {
    titulo: string;
    descripcion: string;
    prioridad: PrioridadTarea;
  }): void {
    const nuevaTarea: Tarea = {
      id: Date.now(),
      titulo: datos.titulo.trim(),
      descripcion: datos.descripcion.trim(),
      prioridad: datos.prioridad,
      completada: false
    };

    this.actualizarTareas([nuevaTarea, ...this.tareasSignal()]);
  }

  cambiarEstado(id: number, completada: boolean): void {
    this.actualizarTareas(
      this.tareasSignal().map((tarea) =>
        tarea.id === id ? { ...tarea, completada } : tarea
      )
    );
  }

  eliminarTarea(id: number): void {
    this.actualizarTareas(this.tareasSignal().filter((tarea) => tarea.id !== id));
  }

  private actualizarTareas(tareas: Tarea[]): void {
    this.tareasSignal.set(tareas);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tareas));
  }

  private cargarTareas(): Tarea[] {
    const guardadas = localStorage.getItem(STORAGE_KEY);

    if (!guardadas) {
      return [
        {
          id: 1,
          titulo: 'Preparar exposicion de biologia',
          descripcion: 'Ordenar diapositivas y repasar puntos clave.',
          prioridad: 'Alta',
          completada: false
        },
        {
          id: 2,
          titulo: 'Resolver practica de matematicas',
          descripcion: 'Completar ejercicios de matrices y sistemas.',
          prioridad: 'Media',
          completada: false
        },
        {
          id: 3,
          titulo: 'Entregar resumen de historia',
          descripcion: 'Subir el documento final a la plataforma.',
          prioridad: 'Baja',
          completada: true
        }
      ];
    }

    try {
      return JSON.parse(guardadas) as Tarea[];
    } catch {
      localStorage.removeItem(STORAGE_KEY);
      return [];
    }
  }
}
