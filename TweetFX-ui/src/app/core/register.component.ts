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
  templateUrl: 'register.component.html'
})


export class RegisterComponent implements OnInit {
  title = 'app';

  username = '';
  password='';
  email='';
  clickedLogin: boolean = false;
  invalid_login: string = "";

  constructor(private service: Service, private router: Router, private sanitization: DomSanitizer) {
  }
  ngOnInit() {

  }

  register() {
    
    if (this.username.length > 0 && this.password.length > 0 && this.email.length>0) {
      this.invalid_login="";
      this.service.register(this.username,this.password,this.email).subscribe(x=>{
        var serviceData=x as JSON;
        if(serviceData['status']=='successful'){
            this.clickedLogin = true;
            sessionStorage.setItem("Username",this.username);
            this.router.navigateByUrl('search');
        }
        else{
            this.clickedLogin = false;
            this.invalid_login=serviceData["status"];
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