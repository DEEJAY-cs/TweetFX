import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { environment } from '../../environments/environment';

@Component({
  moduleId: module.id,
  templateUrl: 'home.component.html'
})
export class HomeComponent implements OnInit {
  
  jwt: any;

  constructor(private router: Router, private title: Title) { 
   
  }

  ngOnInit() {
    
    
  }

  getClass(): string {
    const navHidden = sessionStorage.getItem('navHidden');

    if (navHidden === 'true') {
      return 'homechild-nonav';
    }
    return 'homechild h-75';
  }
}
