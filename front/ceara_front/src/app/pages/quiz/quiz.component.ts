import { Component } from '@angular/core';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-quiz',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent, RouterModule],
  templateUrl: './quiz.component.html',
  styleUrl: './quiz.component.sass'
})
export class QuizComponent {
  
  quizzes = [
  { nome: 'Quiz #1', id: 1 },
  { nome: 'Quiz #2', id: 2 },
  { nome: 'Quiz #3', id: 3 },
  { nome: 'Quiz #4', id: 4 }
];

}
