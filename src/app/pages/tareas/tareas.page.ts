import { CommonModule } from '@angular/common';
import { Component, computed, inject, signal } from '@angular/core';
import {
  IonBadge,
  IonButton,
  IonCheckbox,
  IonContent,
  IonFab,
  IonFabButton,
  IonFooter,
  IonHeader,
  IonIcon,
  IonItem,
  IonItemOption,
  IonItemOptions,
  IonItemSliding,
  IonLabel,
  IonList,
  IonProgressBar,
  IonText,
  IonTitle,
  IonToolbar
} from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import { add, trash } from 'ionicons/icons';

import { Tarea } from '../../models/tarea.model';
import { TareasService } from '../../services/tareas.service';

@Component({
  selector: 'app-tareas',
  standalone: true,
  imports: [
    CommonModule,
    IonBadge,
    IonButton,
    IonCheckbox,
    IonContent,
    IonFab,
    IonFabButton,
    IonFooter,
    IonHeader,
    IonIcon,
    IonItem,
    IonItemOption,
    IonItemOptions,
    IonItemSliding,
    IonLabel,
    IonList,
    IonProgressBar,
    IonText,
    IonTitle,
    IonToolbar
  ],
  templateUrl: './tareas.page.html',
  styleUrl: './tareas.page.scss'
})
export class TareasPage {
  private readonly tareasService = inject(TareasService);

  readonly tareas = this.tareasService.tareas;
  readonly pendientes = computed(
    () => this.tareas().filter((tarea) => !tarea.completada).length
  );
  readonly completadas = computed(
    () => this.tareas().filter((tarea) => tarea.completada).length
  );
  readonly progreso = computed(() => {
    const total = this.tareas().length;
    return total === 0 ? 0 : this.completadas() / total;
  });
  readonly filtro = signal<'todas' | 'pendientes' | 'completadas'>('todas');

  readonly tareasFiltradas = computed(() => {
    const tareas = this.tareas();
    const filtroSeleccionado = this.filtro();

    if (filtroSeleccionado === 'pendientes') {
      return tareas.filter((tarea) => !tarea.completada);
    }

    if (filtroSeleccionado === 'completadas') {
      return tareas.filter((tarea) => tarea.completada);
    }

    return tareas;
  });

  constructor() {
    addIcons({
      add,
      trash
    });
  }

  cambiarCompletada(tarea: Tarea, completada: boolean): void {
    this.tareasService.cambiarEstado(tarea.id, completada);
  }

  eliminarTarea(tarea: Tarea): void {
    this.tareasService.eliminarTarea(tarea.id);
  }

  cambiarFiltro(valor: string | number | undefined): void {
    if (
      valor === 'todas' ||
      valor === 'pendientes' ||
      valor === 'completadas'
    ) {
      this.filtro.set(valor);
    }
  }

}
