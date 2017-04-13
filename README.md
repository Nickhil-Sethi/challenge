# INSTRUCTIONS

Hi! Thanks for taking a look at my code challenge. Here's a litte instructional bit about my code:

The algorithm (in scholarship_selection.py) is fairly self explanatory -- it's dynamic programming approach to computing the optimal sequence, and the main function returns a dictionary e.g. {'sequence' : [4,10,2], 'total':80} as suggested in the challenge.

To use the REST API, first change this portion in your own code needed to import the scholarship_selection module (a litle hacky, I know).

sys.path.insert(0,PARENT_DIRECTORY_OF_CHALLENGE)
from challenge import scholarship_selection

To serve the site, run ./app.py, then in a seperate terminal window, run:

curl -i http://localhost:5000/scholarship_api/

The API allows you to post a scholarship array, and get it's corresponding optimal sequence/total. Each array  is assigned an index integer at the time it is posted, which is necesary to retrieve its solution. To post a scholarship array, first store the array as a json object:

{'array' : [[],...,[]]}

then run the following command:

curl -g -i -H Content-Type:application/json -X POST -d "$v" http://localhost:5000/scholarship_api

where v is a variable where your json object is stored. This should print the json object -- note its id number. To retrieve the corresponding sequence, run:

curl -i http://localhost:5000/scholarship_api/INDEX_NUMBER

Thank you! Hope you find this satisfactory. Looking forward to talking soon :)

# Code challenge

Hi! Very excited to see what you can do. Please complete this coding challenge and submit within 7 days.    
Pick either the front-end or back-end challenge (depending on what you're interested in applying for). You can also do both if you want to be considered for both positions.   

For **questions**, create a github issue and we will answer within 24 hours or email us at willfalcon@nextgenvest.com if you'd rather remain anonymous.   
Good luck!!   

### Languages
If you know many languages, that's great!! However, we need you to be python and javascript ninja at a minimum.       
- If you do the Front-end challenge, use javascript.    
- If you do the Back-end challenge, use python.   


### Submit instructions     
1. Create a github repository to use while you implement your challenge.    
2. We'll look at the commit history and workflow as part of the evaluation process.   
3. When you are done, email back with the link to your repo (willfalcon@nextgenvest.com).    
4. Make sure you have a README.md with build instructions for your code.    
5. Have fun!    

## Challenge for Front-End    
Imagine your hardwork has paid off and you've been awarded a financial aid package. However, you have the option of choosing 1 loan from the 4 different loans offered :/ ...   
Your loan options are:    
1. Direct Subsidized Loan ([interest here](https://studentaid.ed.gov/sa/types/loans/interest-rates))   
2. Direct Unsubsidized Loan ([interest here](https://studentaid.ed.gov/sa/types/loans/interest-rates))   
3. A private bank loan at 4.2% interest    
4. A loan from the university at 4.0% interest.   

Your challenge is to build a widget to help you vizualize and pick a loan.    
- The Widget: 
  - This widget should be a chart or a similar tool to help you vizualize the loan payment over time. The widget should have as inputs a loan amount, interest, loan period (in months).    
  - This widget should also show me the current interest rate for that loan. The rates listed above are enough. Figure out how to get the rates from [here] (first rates on the top of the page are enough) (https://studentaid.ed.gov/sa/types/loans/interest-rates) (and yes, I know there isn't an api ;)).      

#### Challenge gotchas    
1. Your widget should be an [angular (1)](https://angularjs.org/) component.   
2. The loan rate information from [here](https://studentaid.ed.gov/sa/types/loans/interest-rates) cannot be done on the front-end. Must be done through a nodejs server.  
3. The other rates for private bank and university can be hardcoded from the instructions above.    

#### Completion checklist    
[ ] Your widget is an angular component    
[ ] Styling is done with SASS    
[ ] Widget shows a graph (or similar) of expected payoff amount given a payoff date           
[ ] Widget can take as input a loan amount (typed into an input box). Ex: 60000  
[ ] Widget can take as input an interest rate (typed into an input box). Ex: 0.05    
[ ] Widget can take as input loan period (in months) (typed into an input box). Ex: 36    
[ ] There exists somewhere on the page the current student loan interest rate. Ex: 0.03   
[ ] The rate is fetched by the nodejs server   
[ ] Your project has a README.md with build instructions   

#### Judging criteria    
1. Met all requirements in checklist   
2. Widget 1 animations are creative    
3. Good coding style   
4. Efficient code    
5. Good and clear commit history   
6. Clear README.md build instructions   


## Challenge for Back-End
Lucky you! Your hacking skills have been recognized and you've been awarded a bunch of scholarships (woot!). The catch is that you can only pick 11 scholarships...    

In this challenge, pick the 11 scholarships that give you the most money! You can only pick sequential scholarships and the product of all scholarships you pick is how much money you'll be awarded! (this school is very cheap, so you only need a few dollars... scholarships are in the range 0-100).  

Scholarships can appear on the same row   
...    
... 1 2 **3 4 5** 6 ...    
...    
    
Or same column   
...    
1    
**2**    
**3**    
**4**    
5    
...    

Or on a diagonal    
...    
... **1** 2 3 ...     
... 1 **3** 5 ...    
... 1 2 **5** ...    
...    

The number of scholarships n is such that n >= 100.    

Once you've implemented your scholarship selection algorithm, build a small REST API that takes in the nxn matrix of scholarships given and returns your selections. An example request is outlined below.    

- Example (can only pick 3 scholarships) (n=5)          
```
1 2 3 4 5    
1 1 2 3 5   
3 4 5 5 5    
3 4 5 9 5    
1 1 5 5 25    
```

Answer: 5 * 9 * 25 = 1125   (this is not wrong, figure out where this pattern is...)    

API Specs:    
POST /max_scholarship     
'Content-Type: application/json'    

Sample json:    
```
{"data": [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]}
```    

Response:    
```
{"sequence": [5,9,25], "total": 1125}
```    
