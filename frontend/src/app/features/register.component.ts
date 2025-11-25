import { Component } from '@angular/core';
import { AuthService } from '../core/auth.service';
import { Router } from '@angular/router';

@Component({ selector: 'app-register', templateUrl: './register.component.html' })
export class RegisterComponent {
  public name: string = '';
  public email: string = '';
  public password: string = '';

  constructor(private auth: AuthService, private router: Router) {}

  public register(): void {
    this.auth.register(this.name, this.email, this.password).subscribe({
      next: () => this.router.navigate(['/login']),
      error: (err) => alert('Register failed: ' + JSON.stringify(err))
    });
  }
}
