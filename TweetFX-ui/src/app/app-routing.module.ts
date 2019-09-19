import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './core/login.component';
import { HomeComponent } from './core/home.component';
import { SearchComponent } from './core/search.component';
import { RegisterComponent } from './core/register.component';


const routes: Routes = [
  {
    path: 'home',
    redirectTo: '',
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'Register',
    component: RegisterComponent
  },
  {
    path: '',
    component: HomeComponent,
    children: [
      {
        path: 'search',
        component: SearchComponent
      }
    ]
  }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
