import { CommonModule } from '@angular/common';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.sass'
})
export class HomeComponent implements OnInit{
  jogadores: any[] = [];

  jogos = [
    {
      data: '09/07/2025',
      local: 'Ilha do Retiro',
      time_casa: 'Sport',
      time_visitante: 'Ceará',
      placar: '2 x 4'
    },
    {
      data: '12/07/2025',
      local: 'Arena Castelão',
      time_casa: 'Stela',
      time_visitante: 'Ceará',
      placar: ' x '
    },
    {
      data: '16/07/2025',
      local: 'Arena Castelão',
      time_casa: 'Ceará',
      time_visitante: 'Corinthians',
      placar: ' x '
    },
    {
      data: '20/07/2025',
      local: 'Beira Rio',
      time_casa: 'Internacional',
      time_visitante: 'Ceará',
      placar: ' x '
    }
  ];
  
  @ViewChild('carrosselJogadores', { static: false }) carrosselJogadores!: ElementRef;
  
  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:8000/api/jogadores/').subscribe({
      next: (data) => {
        this.jogadores = data
      },
      error: (err) => {
        console.error('Erro ao buscar jogadores: ', err);
      }
    })
  }


  scrollJogadores(direcao: 'esquerda' | 'direita') {
    const el = this.carrosselJogadores.nativeElement;
    const scrollQtd = 320;

    if (direcao === 'direita') {
      el.scrollLeft += scrollQtd;
    } else {
      el.scrollLeft -= scrollQtd;
    }
  }
}
