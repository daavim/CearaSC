import { Component, resolveForwardRef } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.sass']
})
export class LoginComponent {
    loginForm = new FormGroup({
      username: new FormControl('', [Validators.required]),
      senha: new FormControl('', [Validators.required])
    });

  constructor(private router:Router, private cliente: HttpClient) {}

  onSubmit() {
    if (this.loginForm.valid) {
      this.cliente
      .post<{ access: string; refresh: string }>(
        'http://localhost:8000/auth/jwt/create/',
        { 
          username: this.loginForm.controls.username.value,
          password: this.loginForm.controls.senha.value
        },
        {
          observe: "response"
        }
      ).subscribe((resp) => {
        const accessToken = resp.body?.access;
        if (accessToken) {
          localStorage.setItem("token", accessToken);
        }
        if (resp.status == 200){
          this.router.navigate(["/home"])
        }
      },(error)=>{
        console.error("Erro no login: ", error)
      });
    }
  }

  goToRegister() {
    this.router.navigate(['/register']);
  }

}
