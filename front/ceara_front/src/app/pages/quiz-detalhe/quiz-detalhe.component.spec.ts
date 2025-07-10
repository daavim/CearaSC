import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuizDetalheComponent } from './quiz-detalhe.component';

describe('QuizDetalheComponent', () => {
  let component: QuizDetalheComponent;
  let fixture: ComponentFixture<QuizDetalheComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuizDetalheComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuizDetalheComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
