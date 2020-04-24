import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { DataService } from '../data.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  constructor(private httpClient: HttpClient, private router: Router, private dataService: DataService) 
  {    }

  ngOnInit(): void {
  }

  createRecommendation(value: string) {
    return this.httpClient.get('http://127.0.0.1:5000/'+ value)
    .subscribe((response: any) => {
      console.log(response);
      this.dataService.recommendation = response;
      this.router.navigate(['/recommendation']);
    })
  }

  createId(value: number){
    return this.httpClient.get('http://127.0.0.1:5000/user/'+ value)
    .subscribe((response: any) => {
      console.log(response);
      this.dataService.existingUserRec = response;
      this.router.navigate(['/user']);
    })
  }
}
