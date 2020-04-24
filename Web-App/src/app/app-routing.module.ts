import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { RecommendationComponent } from './recommendation/recommendation.component';
import { ExistingUserComponent } from './existing-user/existing-user.component';


const routes: Routes = [
  {path: '', component: SearchComponent},
  {path: 'recommendation', component: RecommendationComponent},
  {path: 'user', component: ExistingUserComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
