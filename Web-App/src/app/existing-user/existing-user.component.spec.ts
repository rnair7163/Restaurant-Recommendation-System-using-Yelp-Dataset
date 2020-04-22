import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExistingUserComponent } from './existing-user.component';

describe('ExistingUserComponent', () => {
  let component: ExistingUserComponent;
  let fixture: ComponentFixture<ExistingUserComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExistingUserComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExistingUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
