import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchComponent } from './search/search.component';

import { HttpClientModule, HttpClient } from "@angular/common/http";
import { RecommendationComponent } from './recommendation/recommendation.component';
import { ExistingUserComponent } from './existing-user/existing-user.component';
import { MatCardModule } from "@angular/material/card";
import { RatingModule } from "ng-starrating";

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    RecommendationComponent,
    ExistingUserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatCardModule,
    RatingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
