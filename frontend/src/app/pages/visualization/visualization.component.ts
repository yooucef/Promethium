import { Component, AfterViewInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-visualization',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './visualization.component.html',
    styleUrls: ['./visualization.component.css']
})
export class VisualizationComponent implements AfterViewInit {

    ngAfterViewInit() {
        // Initialize WebGL or Plotly here
        console.log("Seismic Viewer Initialized");
    }
}
