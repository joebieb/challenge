import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service'

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  
  constructor(private auth: AuthService) {}

  // intercept requests and add auth token
  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    const authToken = this.auth.getAuthorizationToken();
    const authRequest = request.clone({
      headers: request.headers.set('Authorization', authToken)
    });

    // console.log(authRequest);

    return next.handle(authRequest);
  }
}
