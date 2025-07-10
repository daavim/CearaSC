import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';

@Component({
  selector: 'app-home',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.sass'
})
export class HomeComponent {
  jogadores = [
  {
    nome: 'Vina',
    posicao: 'Meia',
    idade: 29,
    foto: 'pedro_raul.png'
  },
  {
    nome: 'Richard',
    posicao: 'Goleiro',
    idade: 31,
    foto: 'assets/jogadores/richard.jpg'
  }
];

jogos = [
  {
    data: '06/07/2025',
    time_casa: 'Ceará',
    time_visitante: 'Fortaleza',
    placar: '2 x 1'
  },
  {
    data: '03/07/2025',
    time_casa: 'Ceará',
    time_visitante: 'Palmeiras',
    placar: '1 x 1'
  }
];
}
