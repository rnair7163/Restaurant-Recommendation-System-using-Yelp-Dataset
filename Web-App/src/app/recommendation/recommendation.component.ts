import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})
export class RecommendationComponent implements OnInit {

  constructor(private dataService: DataService) { }

  recommendations :any;
  k: any;
  max = 5;
  isReadOnly = true;
  ngOnInit(): void {
    this.recommendations = this.dataService.recommendation;
    let recs = this.recommendations;
  }
}
