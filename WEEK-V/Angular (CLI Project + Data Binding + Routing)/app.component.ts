import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  title = 'Angular Focus Board';
  selectedView = 'dashboard';
  searchTerm = '';
  tasks = ['Review component inputs', 'Practice route navigation', 'Build a reusable card'];

  selectView(view: string): void {
    this.selectedView = view;
  }

  addTask(): void {
    const task = this.searchTerm.trim();
    if (task) {
      this.tasks.push(task);
      this.searchTerm = '';
    }
  }
}
