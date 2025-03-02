import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
    selector: 'lib-Modlishka',
    templateUrl: './Modlishka.component.html',
    styleUrls: ['./Modlishka.component.css']
})
export class ModlishkaComponent implements OnInit {
    constructor(private API: ApiService) { }

    userInput = '';
    apiResponse = 'Press the button above to get the version';
    configData = '';

    runModlishka():void {
      this.API.request({
        module: 'Modlishka',
        action: 'run_modlishka'
      }, (response) => {
        this.apiResponse = response;
      });
    }

    stopModlishka():void {
      this.API.request({
        module: 'Modlishka',
        action: 'stop_modlishka'
      }, (response) => {
        this.apiResponse = response;
      });
    }

    ngOnInit() {
      this.API.request({
        module: 'Modlishka',
        action: 'get_config'
      }, (response) => {
        this.configData = response.payload;
      });
    }
}
