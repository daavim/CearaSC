import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';

@Component({
  selector: 'app-perfil',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.sass'
})
export class PerfilComponent {

}
