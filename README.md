# DataScraping
## Task 1 : Wikipedia Scraping
For this a python script named wiki_extractor.py has been provided and it takes 3 arguments 
<br> a. keyword : Defines the query search, argument type : string
<br> b. num_urls : Number of wikipedia pages to extract the data from, argument type : integer
<br> c. output : name of the output file, argument type : string

Sample Code Example
```
python wiki_extractor.py --keyword=”Indian Historical Events” --num_urls=100
--output='out.json'
```
<br>

## Task 2 : Extracting PDF content from URLs

Given a list of links/URLs in csv/xlsx (in this case csv is considered)  format Code file , Task2.ipynb gives an output of json file <br>
{
“page-url”: url link to the page ,
“pdf-url”: url link to the pdf,
“paragraph”: text content of entire pdf
}
  <br> in this form. 
  
  Please Note the library requirements in Task 2 are done according to Colab Environment.
  
  Link to output from Task 2 : https://drive.google.com/file/d/1cBweC_aVWqRUswWMWPjPByy5b8SD56-C/view?usp=sharing
