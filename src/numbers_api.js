class NumbersApi {
	constructor() {
		this.api = "http://numbersapi.com"
		this.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
	}

	async getNumberFact(number, type = "trivia", notFound = null) {
		let url = `${this.api}/${number}/${type}`
		if (notFound) {
			url += `?notfound=${notFound}`
		}
		const response = await fetch(
			`${url}?json`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRandomFact(type) {
		const response = await fetch(
			`${this.api}/random/${type}?json`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {NumbersApi}
