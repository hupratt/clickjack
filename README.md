# clickjack
Simple script to test if a page is vulnerable to clickjacking

### Description
Attempts to render the target site in an iframe and places another iframe on top of it as an example attack. Inspired by the PoC html boilerplate provided by OWASP (https://www.owasp.org/index.php/Testing_for_Clickjacking_(OTG-CLIENT-009)#How_to_Test).

### Requirements
python3

### Usage
`python3 clickjack.py <url>`
