import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DataService } from '../data.service';

@Component({
  selector: 'app-existing-user',
  templateUrl: './existing-user.component.html',
  styleUrls: ['./existing-user.component.scss']
})
export class ExistingUserComponent implements OnInit {

  recommendations: any;
  constructor(private dataService: DataService) { 
    this.recommendations = this.dataService.existingUserRec;
  }

  ngOnInit(): void {
  }
}
