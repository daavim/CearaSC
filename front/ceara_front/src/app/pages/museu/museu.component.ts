import { Component } from '@angular/core';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-museu',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './museu.component.html',
  styleUrl: './museu.component.sass'
})
export class MuseuComponent {
  eventos: any[] = [];
  eventoSelecionado: any = null;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:8000/api/museu/').subscribe({
      next: (dados) => {
        this.eventos = dados.map(evento => ({
          ano: evento.ano,
          descricao: evento.descricao,
          img: `${evento.titulo}.png`
        }));
      },
      error: (err) => {
        console.error('Erro ao buscar eventos do museu:', err);
      }
    });
  }

  selecionarEvento(evento: any) {
    this.eventoSelecionado = evento;
  }

}
