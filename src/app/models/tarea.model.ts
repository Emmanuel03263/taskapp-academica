export type PrioridadTarea = 'Alta' | 'Media' | 'Baja';

export interface Tarea {
  id: number;
  titulo: string;
  descripcion: string;
  prioridad: PrioridadTarea;
  completada: boolean;
}
