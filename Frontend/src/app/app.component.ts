import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  // The list of links for the navigation bar
  links = ['Assignments', 'Courses', 'Announcements'];

}
