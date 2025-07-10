import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { PerfilService } from '../../services/perfil.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-perfil',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.sass'
})
export class PerfilComponent implements OnInit{
  usuario: any;

  constructor(private perfilService: PerfilService, private router: Router){}

  ngOnInit(): void {
    this.perfilService.getPerfil().subscribe((dados) => {
      this.usuario = dados;
    })
  }

  logout(): void {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];

    if (file) {
      const formData = new FormData();
      formData.append('foto', file, file.name);

      this.perfilService.updateFoto(formData).subscribe({
        next: (response) => {
          this.perfilService.getPerfil().subscribe(dados => {
            this.usuario = dados;
          })
        },
        error: (err) => {
          console.error('Erro ao fazer upload da foto:', err);
        }
      });
    }
  }

}
