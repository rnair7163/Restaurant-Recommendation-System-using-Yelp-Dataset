import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  recommendation: any;
  existingUserRec: any;
  constructor() { }
}
