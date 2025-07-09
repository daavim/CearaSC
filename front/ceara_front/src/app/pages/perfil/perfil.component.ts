import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from '../../shared/navbar/navbar.component';
import { PerfilService } from '../../services/perfil.service';

@Component({
  selector: 'app-perfil',
  imports: [CommonModule, ReactiveFormsModule, NavbarComponent],
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.sass'
})
export class PerfilComponent implements OnInit{
  usuario: any;

  constructor(private perfilService: PerfilService){}

  ngOnInit(): void {
    this.perfilService.getPerfil().subscribe((dados) => {
      this.usuario = dados;
    })
  }

}
