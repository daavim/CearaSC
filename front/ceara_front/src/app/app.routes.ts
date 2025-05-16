import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { CadastroComponent } from './pages/cadastro/cadastro.component';
import { PerfilComponent } from './pages/perfil/perfil.component';
import { HomeComponent } from './pages/home/home.component';
import { MuseuComponent } from './pages/museu/museu.component';
import { QuizComponent } from './pages/quiz/quiz.component';
import { BolaoComponent } from './pages/bolao/bolao.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'register', component: CadastroComponent },

    { path: 'home', component: HomeComponent },
    { path: 'museu', component: MuseuComponent },
    { path: 'quiz', component: QuizComponent },
    { path: 'bolao', component: BolaoComponent },
    { path: 'perfil', component: PerfilComponent },

    { path: '**', component: HomeComponent }
];
