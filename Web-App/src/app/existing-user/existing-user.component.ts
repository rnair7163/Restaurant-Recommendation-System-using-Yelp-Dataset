import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-existing-user',
  templateUrl: './existing-user.component.html',
  styleUrls: ['./existing-user.component.scss']
})
export class ExistingUserComponent implements OnInit {

  recommendations: any;
  constructor(private httpClient: HttpClient) { 
    this.httpClient.get('http://127.0.0.1:5000/id/1')
    .subscribe((response: any) => {
      console.log(response);
      this.recommendations = response;
    })
  }

  ngOnInit(): void {
  }
}
