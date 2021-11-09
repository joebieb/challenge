import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  // regular angular form
  
  // TODO: change handling of base url - hardcoding for now
  authUrl = 'http://localhost:8000/api/auth/token';  
  responseError: string;

  constructor(private http: HttpClient, private auth: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit(form: NgForm) {
    console.log(form.value.email);
    const headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    const data = {email: form.value.email};
    this.http.post(this.authUrl, data, { headers: headers })
      .toPromise()
      .then((tokenData:any) => {
        this.auth.setAuthorizationToken(tokenData.access_token);
        console.log(this.auth.getAuthorizationToken());
        
        this.router.navigate(['/quote']);
    },(err:HttpErrorResponse)=>{
      // TODO: handle errors more intelligently, just displaying them on the page
      // console.log(err);
      this.responseError = err.message;
    })
  }
}
