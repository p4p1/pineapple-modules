import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
    selector: 'lib-Modlishka',
    templateUrl: './Modlishka.component.html',
    styleUrls: ['./Modlishka.component.css']
})
export class ModlishkaComponent implements OnInit {
    constructor(private API: ApiService) { }

    ngOnInit() {
    }
}
