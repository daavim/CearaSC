import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { CadastroComponent } from './pages/cadastro/cadastro.component';
import { PerfilComponent } from './pages/perfil/perfil.component';
import { HomeComponent } from './pages/home/home.component';
import { MuseuComponent } from './pages/museu/museu.component';
import { QuizComponent } from './pages/quiz/quiz.component';
import { authGuard } from './auth.guard';
import { QuizDetalheComponent } from './pages/quiz-detalhe/quiz-detalhe.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'register', component: CadastroComponent },

    { path: 'home', component: HomeComponent, canActivate: [authGuard] },
    { path: 'museu', component: MuseuComponent, canActivate: [authGuard] },
    { path: 'perfil', component: PerfilComponent, canActivate: [authGuard] },
    { path: 'quiz', component: QuizComponent, canActivate: [authGuard] },
    { path: 'quiz/:id', component: QuizDetalheComponent, canActivate: [authGuard] },

    { path: '**', component: LoginComponent }
];
