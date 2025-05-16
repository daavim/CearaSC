import { Component } from '@angular/core';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-museu',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './museu.component.html',
  styleUrl: './museu.component.sass'
})
export class MuseuComponent {

}
