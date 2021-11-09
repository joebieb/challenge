import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-quotation',
  templateUrl: './quotation.component.html',
  styleUrls: ['./quotation.component.scss']
})
export class QuotationComponent implements OnInit {
  // my first attempt at using ReactiveForms
  // TODO: create types/interfaces instead of using "any"

  quotationForm: FormGroup;
  minDate: Date;
  currentQuote: any;
  responseError: string;

  dateRange = this.fb.group({
    start: ['',[
      Validators.required
    ]],
    end: ['',[
      Validators.required
    ]]
  }) 

  currencies: any[] = [
    {value: 'EUR', viewValue: 'EUR'},
    {value: 'GBP', viewValue: 'GBP'},
    {value: 'USD', viewValue: 'USD'},
  ];

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.minDate = new Date();
   }

  ngOnInit(): void {
    this.quotationForm = this.fb.group({
      age: [18,[
        Validators.required,
        Validators.pattern('^\\d+(?:,\\d+)*$'),
        Validators.min(18)
      ]],
      currency: ['EUR',[
        Validators.required
      ]],
      dates: this.dateRange,
    })

    // this.quotationForm.valueChanges.subscribe(console.log)
  }

  get age() {
    return this.quotationForm.get('age')
  }

  getQuote() {
    // reset error text if exists
    this.responseError = '';

    // TODO: change handling of base url - hardcoding for now
    const quotationUrl = 'http://localhost:8000/api/quotation'
    const headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    const data = {
      age: this.quotationForm.value.age.toString().split(',').map(Number),
      currency_id: this.quotationForm.value.currency,
      start_date: this.quotationForm.value.dates.start.toISOString().slice(0, 10),
      end_date: this.quotationForm.value.dates.end.toISOString().slice(0, 10)
    };

    this.http.post(quotationUrl, data, { headers: headers }).toPromise().then((_result:any) => {
      console.log(_result)
      this.currentQuote = _result;
      this.currentQuote.total = (Math.round(this.currentQuote.total * 100) / 100).toFixed(2);
    },(err:HttpErrorResponse)=>{
      // TODO: handle errors more intelligently, just displaying them on the page
      // console.log(err);
      this.responseError = err.message;
    })
  }
}
