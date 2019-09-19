import { Injectable } from '@angular/core';
import {
    HttpClient,
    HttpHeaders
  } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable()
export class Service {

  constructor(private http: HttpClient) {
  }

  private extractData(res: any) {
    const body = res;
    return body;
  }

  login(username,password) {
    return this.http.get(`http://127.0.0.1:5002/login/${username}/${password}`);  
  }

  register(username, password , email){
    return this.http.get(`http://127.0.0.1:5002/register/${username}/${password}/${email}`);
  }

  twitterSearch(searchTerm) {
    const serviceUrl = `http://127.0.0.1:5002/twitterSearch/${searchTerm}`;
    return this.http.get(serviceUrl);
  }

  saveTweetsToDB(labelledTweets) {
    const serviceUrl = `http://127.0.0.1:5002/saveTweetsToDB`;
    return this.http
      .post(serviceUrl, labelledTweets);
  }

  

} 