import { Component, OnInit, HostListener } from '@angular/core';
import { Service } from '../service/service';
import {
  DomSanitizer,
  SafeHtml,
  SafeUrl,
  SafeStyle
} from '@angular/platform-browser';

import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';
;

@Component({
  moduleId: module.id,
  templateUrl: 'login.component.html'
})


export class LoginComponent implements OnInit {
  title = 'app';

  username = '';
  password='';
  clickedLogin: boolean = false;
  invalid_login: string = "";

  constructor(private service: Service, private router: Router, private sanitization: DomSanitizer) {
  }
  ngOnInit() {

  }

  login() {
    
    if (this.username.length > 0 && this.password.length > 0) {
      this.invalid_login="";
      this.service.login(this.username,this.password).subscribe(x=>{
        var serviceData=x as JSON;
        if(serviceData['username']==this.username){
            this.clickedLogin = true;
            sessionStorage.setItem("Username",this.username);
            this.router.navigateByUrl('search');
        }
        else{
            this.clickedLogin = false;
            this.invalid_login=serviceData["username"];
        }
      }, error => {
        //console.log("error", error);
        if (error.error["error"] !== undefined) {
          this.invalid_login = error.error["error_description"];
        }
      });
      
    }

  }
}