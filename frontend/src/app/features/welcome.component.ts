import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({ selector: 'app-welcome', templateUrl: './welcome.component.html' })
export class WelcomeComponent {
  constructor(private router: Router) {}

  public goToInvite(): void {
    this.router.navigate(['/invite']);
  }

  public goToLogin(): void {
    this.router.navigate(['/login']);
  }
}
