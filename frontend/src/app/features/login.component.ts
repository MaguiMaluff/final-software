import { Component } from '@angular/core';
import { AuthService } from '../core/auth.service';
import { Router } from '@angular/router';

@Component({ selector: 'app-login', templateUrl: './login.component.html' })
export class LoginComponent {
  public email: string = '';
  public password: string = '';

  constructor(private auth: AuthService, private router: Router) {}

  public login(): void {
    this.auth.login(this.email, this.password).subscribe({
      next: () => this.router.navigate(['/invite']),
      error: () => alert('Login failed')
    });
  }

  public goToRegister(): void {
    this.router.navigate(['/register']); // Ensure this matches the route in app.module.ts
  }
}
