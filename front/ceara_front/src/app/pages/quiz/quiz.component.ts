import { Component, OnInit } from '@angular/core';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-quiz',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent, RouterModule],
  templateUrl: './quiz.component.html',
  styleUrl: './quiz.component.sass'
})
export class QuizComponent implements OnInit{

  quizzes: { id: number, titulo: string }[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<{ id: number, titulo: string }[]>('http://localhost:8000/api/quiz/')
      .subscribe({
        next: (res) => {
          this.quizzes = res;
        },
        error: (err) => {
          console.error('Erro ao buscar quizzes:', err);
        }
      });
  }

}
