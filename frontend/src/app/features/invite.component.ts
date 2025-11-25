import { Component } from '@angular/core';
import { NotificationService } from '../core/notification.service';

@Component({ selector: 'app-invite', templateUrl: './invite.component.html' })
export class InviteComponent {
  public email: string = '';

  constructor(private notif: NotificationService) {}

  public sendInvite(): void {
    try{


    this.notif.sendInvite(this.email).subscribe({
      next: () => alert('Invitation sent'),
      error: () => alert('Failed to send invitation')
    });
    } catch (e) {
      alert('An unexpected error occurred');
      console.error(e);
    }
  }
}
