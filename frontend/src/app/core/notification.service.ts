import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class NotificationService {
  private base = 'http://localhost:5000/invite';
  constructor(private http: HttpClient) {}

  sendInvite(email: string) {
    return this.http.post(this.base, { email });
  }
}
