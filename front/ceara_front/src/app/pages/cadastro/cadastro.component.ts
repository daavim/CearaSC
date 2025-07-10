import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.sass'
})
export class CadastroComponent {
  cadastroForm = new FormGroup({
    username: new FormControl("", [Validators.required]),
    senha: new FormControl("", [Validators.required]),
    confirmSenha: new FormControl("", [Validators.required]),
  })

  constructor(private router:Router, private cliente: HttpClient) {}

  onSubmit(){
    if (this.cadastroForm.valid) {
      this.cliente
      .post<{ access: string; refresh: string }>(
        'http://localhost:8000/auth/users/',
        { username: this.cadastroForm.controls.username.value,
          password: this.cadastroForm.controls.senha.value,
          re_password: this.cadastroForm.controls.confirmSenha.value 
        },
        { observe: 'response'}
      )
      .subscribe((resp) => {
        if (resp.status == 201){
          this.router.navigate(['/login'])
        }
      });
    }
  }
}
