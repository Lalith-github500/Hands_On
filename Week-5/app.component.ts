// app.component.ts
// Week 5 - Frontend Frameworks
// Demonstrates: Angular CLI project structure, data binding
// (interpolation, property binding, two-way binding with ngModel,
// event binding), and routing between Home / About pages.
//
// Project setup (Angular CLI):
//   npm install -g @angular/cli
//   ng new my-angular-app --routing --standalone=false
//   cd my-angular-app
//   ng generate component home
//   ng generate component about
//   Replace src/app/app.component.ts (and .html) with the code below,
//   and wire up app-routing.module.ts as shown further down.
//   ng serve

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <nav class="navbar">
      <a routerLink="/home" routerLinkActive="active">Home</a>
      <a routerLink="/about" routerLinkActive="active">About</a>
    </nav>

    <main>
      <h1>{{ pageTitle }}</h1> <!-- Interpolation -->

      <!-- Property binding: disable button based on component state -->
      <button [disabled]="isSaving" (click)="onSave()">
        {{ isSaving ? 'Saving...' : 'Save' }}
      </button>

      <!-- Two-way binding with ngModel (requires FormsModule) -->
      <label>
        Your name:
        <input type="text" [(ngModel)]="username" placeholder="Enter name" />
      </label>
      <p>Hello, {{ username || 'stranger' }}!</p>

      <!-- Event binding -->
      <button (click)="incrementClicks()">Click me</button>
      <p>Button clicked {{ clickCount }} time(s).</p>

      <!-- Routed child views render here -->
      <router-outlet></router-outlet>
    </main>
  `,
  styles: [
    `
      .navbar a { margin-right: 1rem; text-decoration: none; }
      .navbar a.active { font-weight: bold; color: #1976d2; }
      main { padding: 1rem; font-family: sans-serif; }
    `,
  ],
})
export class AppComponent {
  pageTitle = 'Angular Data Binding Demo';
  isSaving = false;
  username = '';
  clickCount = 0;

  onSave(): void {
    this.isSaving = true;
    // simulate an async save operation
    setTimeout(() => {
      this.isSaving = false;
    }, 1500);
  }

  incrementClicks(): void {
    this.clickCount++;
  }
}

/* ------------------------------------------------------------------
 * app-routing.module.ts (create this file alongside app.component.ts)
 * ------------------------------------------------------------------
 *
 * import { NgModule } from '@angular/core';
 * import { RouterModule, Routes } from '@angular/router';
 * import { HomeComponent } from './home/home.component';
 * import { AboutComponent } from './about/about.component';
 *
 * const routes: Routes = [
 *   { path: '', redirectTo: '/home', pathMatch: 'full' },
 *   { path: 'home', component: HomeComponent },
 *   { path: 'about', component: AboutComponent },
 * ];
 *
 * @NgModule({
 *   imports: [RouterModule.forRoot(routes)],
 *   exports: [RouterModule],
 * })
 * export class AppRoutingModule {}
 *
 * ------------------------------------------------------------------
 * app.module.ts must import FormsModule (for ngModel) and
 * AppRoutingModule:
 *
 * import { FormsModule } from '@angular/forms';
 * imports: [BrowserModule, AppRoutingModule, FormsModule]
 * ------------------------------------------------------------------
 */
