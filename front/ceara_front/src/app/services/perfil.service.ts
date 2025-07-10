import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PerfilService {
  private apiUrl = 'http://localhost:8000/api/perfil/';

  constructor(private http: HttpClient) {}

  getPerfil(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  updateFoto(formData: FormData): Observable<any> {
    return this.http.patch(`http://localhost:8000/api/perfil/foto/`, formData);
  }
}
