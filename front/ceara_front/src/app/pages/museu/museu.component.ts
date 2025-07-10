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
    eventoSelecionado: any = null;

  eventos = [
    {
      ano: '1914',
      img: 'escudo1914.svg',
      descricao: 'Fundação do clube com o nome "Rio Branco Foot-Ball Club", usando as cores lilás e branco.'
    },
    {
      ano: '1915',
      img: 'escudo1915.svg',
      descricao: 'Mudança do nome para Ceará Sporting Club e adoção das cores preta e branca.'
    },
    {
      ano: '1955',
      img: 'escudo1955.svg',
      descricao: 'Conquista do Campeonato Cearense de forma invicta, reforçando a tradição do Vozão.'
    },
    {
      ano: '1969',
      img: 'escudo1969.svg',
      descricao: 'Ano marcante com a modernização da estrutura do clube e novos títulos estaduais.'
    }
  ];

  selecionarEvento(evento: any) {
    this.eventoSelecionado = evento;
  }

}
