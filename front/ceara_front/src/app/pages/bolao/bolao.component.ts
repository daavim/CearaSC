import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';

@Component({
  selector: 'app-bolao',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './bolao.component.html',
  styleUrl: './bolao.component.sass'
})
export class BolaoComponent {

}
