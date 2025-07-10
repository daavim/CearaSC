import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-quiz-detalhe',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './quiz-detalhe.component.html',
  styleUrl: './quiz-detalhe.component.sass'
})
export class QuizDetalheComponent implements OnInit{
  quizId: string | null = null;
  quiz: any;
  perguntas: any[] = [];
  respostas: { [perguntaId: number]: number } = {};

  constructor(private router: Router, private route: ActivatedRoute, private http: HttpClient){}

  ngOnInit(): void {
    this.quizId = this.route.snapshot.paramMap.get('id');

    if (this.quizId) {
      this.http.get(`http://localhost:8000/api/quiz/${this.quizId}/completo/`)
        .subscribe(data => {
          this.quiz = data;
          this.perguntas = (data as any)['perguntas'];
        });
    }
  }

  onSelecionarAlternativa(perguntaId: number, alternativaId: number): void {
    this.respostas[perguntaId] = alternativaId;
  }


  calcularPontuacao(): number {
    let score = 0;

    for (const pergunta of this.perguntas) {
      const respostaSelecionada = this.respostas[pergunta.id];
      const alternativaCorreta = pergunta.alternativas.find((alt: any) => alt.correta);

      if (respostaSelecionada && alternativaCorreta?.id === respostaSelecionada) {
        score++;
      }
    }

    return score;
  }

  finalizarQuiz(): void {
    const pontuacao = this.calcularPontuacao();

    const historicoData = {
      tipo: 'quiz',
      titulo: this.quiz?.titulo || `Quiz #${this.quizId}`,
      descricao: `Você acertou ${pontuacao} de ${this.perguntas.length} perguntas.`
    };

    this.http.post('http://localhost:8000/api/historico/', historicoData).subscribe({
      next: () => {
        alert('Resultado salvo com sucesso!');
        this.router.navigate(['/perfil']);
      },
      error: (err) => {
        console.error('Erro ao salvar histórico:', err);
        console.log('Detalhes do erro:', err.error);
      }
    });
  }

}
