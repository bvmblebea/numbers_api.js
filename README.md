# numbers_api.js
Web-API for [numbersapi.com](http://numbersapi.com) website which is an api to get interesting facts about numbers

## Example
```JavaScript
async function main() {
	const { NumbersApi } = require("./numbers_api.js")
	const numbersApi = new NumbersApi()
	const randomFact = await numbersApi.getRandomFact("type")
	console.log(randomFact)
}

main()
```
