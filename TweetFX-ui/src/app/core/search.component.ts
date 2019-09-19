import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { environment } from '../../environments/environment';

@Component({
  moduleId: module.id,
  templateUrl: 'search.component.html'
})
export class SearchComponent implements OnInit {
  
  jwt: any;

  constructor(private router: Router, private title: Title) { 
   
  }

  ngOnInit() {
    
    
  }

}
