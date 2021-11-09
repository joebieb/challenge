import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  authToken: string;
  
  constructor() { 
    // default correctly formatted but invalid token
    this.authToken = 'Bearer xx.yy.zz';
  }

  getAuthorizationToken() {
    return this.authToken;
  }

  setAuthorizationToken(token: string) {
    this.authToken = `Bearer ${token}`;
  }
}
