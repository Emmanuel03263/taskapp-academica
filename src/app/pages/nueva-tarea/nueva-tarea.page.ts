import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import {
  IonBackButton,
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonInput,
  IonItem,
  IonNote,
  IonTextarea,
  IonTitle,
  IonToolbar
} from '@ionic/angular/standalone';

import { PrioridadTarea } from '../../models/tarea.model';
import { TareasService } from '../../services/tareas.service';

@Component({
  selector: 'app-nueva-tarea',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    IonBackButton,
    IonButton,
    IonButtons,
    IonContent,
    IonHeader,
    IonInput,
    IonItem,
    IonNote,
    IonTextarea,
    IonTitle,
    IonToolbar
  ],
  templateUrl: './nueva-tarea.page.html',
  styleUrl: './nueva-tarea.page.scss'
})
export class NuevaTareaPage {
  private readonly fb = inject(FormBuilder);
  private readonly router = inject(Router);
  private readonly tareasService = inject(TareasService);

  intentoEnviar = false;

  readonly formulario = this.fb.nonNullable.group({
    titulo: ['', [Validators.required, Validators.minLength(5)]],
    descripcion: ['', [Validators.required, Validators.maxLength(120)]],
    prioridad: ['Media' as PrioridadTarea, [Validators.required]]
  });

  guardarTarea(): void {
    this.intentoEnviar = true;

    if (this.formulario.invalid) {
      this.formulario.markAllAsTouched();
      return;
    }

    this.tareasService.agregarTarea(this.formulario.getRawValue());
    void this.router.navigateByUrl('/');
  }

  cancelar(): void {
    void this.router.navigateByUrl('/');
  }

  mostrarError(campo: 'titulo' | 'descripcion'): boolean {
    const control = this.formulario.controls[campo];
    return control.invalid && (control.touched || this.intentoEnviar);
  }
}
