import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./pages/tareas/tareas.page').then((m) => m.TareasPage)
  },
  {
    path: 'nueva-tarea',
    loadComponent: () =>
      import('./pages/nueva-tarea/nueva-tarea.page').then(
        (m) => m.NuevaTareaPage
      )
  }
];
