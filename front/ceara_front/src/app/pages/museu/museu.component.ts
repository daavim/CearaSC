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
      ano: 1915,
      descricao: 'Fundação do Ceará Sporting Club.',
      img: 'escudo1915.svg'
    },
    {
      ano: 1918,
      descricao: 'Primeiro Clássico-Rei oficial: Ceará 2x0 Fortaleza.',
      img: 'escudo1918.svg'
    },
    {
      ano: 1964,
      descricao: 'Conquista da Taça Brasil – Zona Norte-Nordeste.',
      img: 'escudo1964.svg'
    },
    {
      ano: 1994,
      descricao: 'Vice-campeão da Copa do Brasil.',
      img: 'escudo1994.svg'
    },
    {
      ano: 2015,
      descricao: '1º título da Copa do Nordeste.',
      img: 'escudo2015.svg'
    },
    {
      ano: 2022,
      descricao: 'Quartas da Copa Sul-Americana — melhor campanha internacional.',
      img: 'escudo2022.svg'
    },
    {
      ano: 2023,
      descricao: 'Conquista da 47ª edição do Cearense e reformulação com base e estrangeiros.',
      img: 'escudo2023.svg'
    },
    {
      ano: 2024,
      descricao: 'Títulos Sub-15, 17 e 20 + criação do departamento feminino.',
      img: 'escudo2024.svg'
    }
  ];


  selecionarEvento(evento: any) {
    this.eventoSelecionado = evento;
  }

}
