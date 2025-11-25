import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private base = 'http://localhost:5000/auth';
  constructor(private http: HttpClient) {}

  register(name: string, email: string, password: string) {
    return this.http.post(`${this.base}/register`, { name, email, password });
  }

  login(email: string, password: string) {
    return this.http.post<any>(`${this.base}/login`, { email, password })
      .pipe(tap(res => {
        if (res && res.access_token) {
          localStorage.setItem('access_token', res.access_token);
        }
      }));
  }

  logout() {
    localStorage.removeItem('access_token');
  }

  getToken() {
    return localStorage.getItem('access_token');
  }

  isAuthenticated() {
    return !!this.getToken();
  }
}
