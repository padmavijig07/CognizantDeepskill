# Angular CLI-Style Example

This folder demonstrates the main Week 5 Angular concepts in a compact standalone component shape. In a real Angular CLI project, these files belong under `src/app`.

- Interpolation: `{{ title }}` and `{{ selectedView }}`
- Property binding: `[value]="searchTerm"`
- Event binding: `(click)="selectView('tasks')"`
- Two-way binding: `[(ngModel)]="searchTerm"`
- Routing concept: view links call `selectView` and update the visible panel

Create a full project with `ng new angular-demo`, then copy the component files into `src/app` and import `FormsModule` for `ngModel`.
