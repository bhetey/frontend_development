# SmartPay 
## Build & Style The UI : Challenge 1 of 4 
### Step 1

- [x] Style the BODY element with a white background color.

- [x] Within the BODY tag, create a DIV and give it a data-cart-info attribute. Inside this DIV, create a HEADING element with mdc-typography--headline4" as its CSS class.

- [x] The HEADING element should have 2 SPAN children elements. The First SPAN element displays a shopping cart by setting it's CSS class to material-icons and its content to shopping_cart. The second SPAN element should have a data-bill attribute and will be used to display the total figure the user is trying to pay on the app.

- [x] Create another DIV just after the data-cart-info DIV. Give this new DIV a data-credit-card attribute and set its class to mdc-card and mdc-card--outlined . Within the data-credit-card DIV you just created, add a new DIV with a class of mdc-card__primary-action. These elements will be styled with the look and feel of an actual credit card. Brace yourself!

- [x] Within the .mdc-card__primary-action DIV, create an IMAGE with an attribute of data-card-type and set its source to [https://placehold.it/120x60.png?text=Card](https://placehold.it/120x60.png?text=Card). This IMAGE will be used to display the credit card type (Visa or MasterCard), based on the series of numbers entered by the user.

- [x] Right after the IMAGE and still within the mdc-card__primary-action DIV, create a new DIV with an attribute of data-cc-digits. It should contain four INPUT text fields, each with a size of 4 and a placeholder of ---- (4 dashes). These fields will be used to collect the credit card numbers from the user.

- [x] Create a DIV with an attribute of data-cc-info as a sibling to the data-cc-digits DIV. This new DIV should have two INPUT text fields, one for entering the card holder's name while the other will be for the card's expiry date. The first field should have a size of 20 and a placeholder of Name Surname. The expiry date field should have a size of 6 and a placeholder of MM/YY - indicating the expiry date format.

> We are now done with the structure of the credit card component. Let's make a button to allow the user make payment with the card details

- [x] Create a BUTTON as a sibling to the data-credit-card DIV. Set the BUTTON's class to mdc-button and give it a data-pay-btn attribute. It should have Pay Now as its display text. After the user enters details of the card and clicks on this button, the app will strike-though the card details that are in-valid, if any.

### Step 2

> While we might have the right structure in place, the app visually tells a different story. Time to make the app look good and usable.

- [x] The SPAN elements within the data-cart-info DIV should be displayed as inline block elements and their vertical-align set to middle. The .material-icons SPAN should have a 150 pixels size of font.

- [x] Give the data-credit-card DIV 435px width, 240px minimum height, 10px rounded borders, and a #5d6874 background colour.

- [x] Display the data-card-type IMAGE as a block element. Give it a 120px width and a 60px height.

- [x] The data-cc-digits DIV should have a 2em top margin.

- [x] INPUT elements in the data-cc-digits DIV should have a white color, 2em font size and line height, no border or background, and a right margin of 0.5em;

- [x] The data-cc-info DIV should have a 1em top margin.

- [x] INPUT elements in the data-cc-info DIV should have a white color, 1.2em font size, no border and no background. The second input should also have a right padding of 10px and be floated to the right of the viewport.

- [x] The data-pay-btn BUTTON should have a fixed position, 90% width, a solid border of 1px and positioned 20px from the bottom of the viewport.

> Your app should look better at this point. Ideally, the 4 input fields within the data-cc-digits DIV should all be on a single horzontal line.

## Get The Bill : Challenge 2 of 4 
> Write all Javascript strictly in ES6 syntax. This means use arrow functions instead of the function keyword. Declare variables and functions with `const` or `let`. Use `const` by default, and only use let if you are sure you need to re-assign values to the said variable. Use the [Selector API](https://mygradr.web.app/kugMbar7bNPd1cS3evDL/[https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)) instead of the getElementBy... or getElementsBy... APIs. 
> Install the [JSON Viewer Chrome extension](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en), open a new tab and go to this [API endpoint](https://randomapi.com/api/006b08a801d82d0c9824dcfdfdfa3b3c). You will be making HTTP requests to the API, so spend some time looking at the structure of the response data.

### Step 1
- [x] Within the SCRIPT element and just after the `billHype` function, create an `appState` variable and assign it an empty Object literal. This variable will hold data for the app.

- [x] Create a `formatAsMoney` function. It should take in an `amount` and a `buyerCountry` parameter. It will use these parameters to format the user's bill as a proper currency.

- [x] Create `detectCardType`, `validateCardExpiryDate`, and `validateCardHolderName` functions. detectCardType should be declared to accept `first4Digits` as a parameter. As implied by their names, these functions will play major roles in validating various aspects of the card being used for payment

- [x] Create a `uiCanInteract` function. It will be called to setup the UI, including adding event handlers to enable interactions with the app.

- [x] Create a `displayCartTotal` function. It should expect a parameter and should use object de-structuring to obtain the `results` property of the given parameter. This function will be called with the data from an API call and it will display the total bill to be paid. [Read More on Object Destructing](https://hacks.mozilla.org/2015/05/es6-in-depth-destructuring/), [ES6 Destructuring: The Complete Guide](https://codeburst.io/es6-destructuring-the-complete-guide-7f842d08b98f), [Destructuring assignment
](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

### Step 2

- [x] Update the `fetchBill` function. It should then use the browser's `fetch` function to make a HTTP request to `apiEndpoint`. Using an arrow function in a `.then` call to the `fetch` function, return the response after converting it to JSON. Using another `.then` call to the first one, pass the JSON data to `displayCartTotal`. Make sure to handle errors that may occur, e.g by showing a warning message in the console.
> Uselinks : 
* [Google Web Developers Introduction to fetch](https://developers.google.com/web/updates/2015/03/introduction-to-fetch)
* [MDN Fetch Api](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

- [x] Call the `fetchBill` function from inside the `startApp`. This should be the only code or function call within `startApp`.

### Step 3 

- [x] In the body of the `displayCartTotal` function, de-structure the first item in the results array parameter into a data variable. Next, use object de-structuring to obtain the `itemsInCart` and `buyerCountry` properties from `data`. You might want to install the [JSONViewer Chrome extension](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en), open a new tab and navigate to `https://randomapi.com/api/006b08a801d82d0c9824dcfdfdfa3b3c` to see the shape of the JSON data we are dealing with.

- [x] Next, `displayCartTotal` should set `appState.items` to `itemsInCart` and `appState.country` to `buyerCountry`.

- [x] Use the Array `.reduce` function to calculate the total bill from `itemsInCart` Note that each item has a qty property indicating how many of that item the user bought. Assign the calculated bill to `appState.bill`

- [x] Go back to the formatAsMoney function. Use the in-built javascript `.toLocaleString` function on the amount and `buyerCountry` parameters to format amount as a currency with the currency symbol of `buyerCountry`. The countries and their currency symbols are in the countries array you got in your starter code. If the `buyerCountry` is not in countries, then use United States as the country and format the currency accordingly.

- [x] Continuing from where you left off in `displayCartTotal`, use the `formatAsMoney` function to set `appState.billFormatted` to the formatted total bill. The already assigned `appState.bill` and `appState.country` should be handy for this task!

- [x] Set the text content of the data-bill SPAN element to the formatted bill saved in `appState.billFormatted`

- [x] Assign an array literal to `appState.cardDigits`

- [x] Finally, call `uiCanInteract` to wrap up `displayCartTotal`

> Run your app (click the play button) and see if the correct total bill is displayed in the UI with the right currency format. Next, we will allow input and interaction so that users can provide payment information.

## Handle Simple Validation : Challenge 3 of 4
### Step 1 
- [x] Create a `flagIfInvalid` function just after `formatAsMoney` function. This function is used to mark an input entry as invalid (strike-though) nor not. It should take a `field` and `isValid` parameters. If `isValid` is true, it should remove the `is-invalid` class from `field`, otherwise it should add it to `field`.

- [x] Just after `flagIfInvalid` function, create a `expiryDateFormatIsValid` function which takes a field parameter representing the card's expiry date `field`. It should return true if the field's value complies with the MM/YY format, otherwise it should return false.

- [x] With the above utility functions out of the way, go back to the `validateCardExpiryDate` function. This function should return true if the value provided matches the `MM/YY` format (hint: delegate to expiryDateFormatIsValid) AND if the date is in the future. In either case, it should use the `flagIfInvalid` function to mark the field as valid or not. It then has to return true or false depending on if the validation requirements are met or not.

- [x] Now to the `validateCardHolderName` function. Recall that its placeholder already suggests the required format, which is Name Surname (2 names separated by space). Each name should be at least 3 characters long. It should use the `flagIfInvalid` function to mark the field as valid or not and then return true or false depending on if the validation requirements are met or not.

