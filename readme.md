# Python Password Cracker Exercise

<p>This exercise is used to teach students string manipulation through generating different string combinations and the Python requests library by making the students try these different string combinations as password in a post requests to an authentication server.</p>

## Prompt for students

<p>Time to put your Python skills into hacking. Your job will be to brute force an authentication server using Python to generate all possible password combinations. The length of the password can be from 1 character to 5 characters and can include all the English Alphabet and the numbers 0 through 9, special characters are not included.</p>

<p>What we know</p>
<ul>
  <li>We overheard someone say their username was "mike" at coffee shop next the building we are hacking</li>
  <li>By sending junkmail to the workers at the building with a promise of a free cruise for anyone who could turn in the correct IP address of there authentication server we were able to get the IP of PUTIPHERE </li>
</ul>

<br>
<br>

<p>1. Make a new python file and brain storm a way to generate all possible password combinations using sequential string generation. Take each possible password and put it into a list.</p>

<p>Link if the students struggle: https://stackoverflow.com/questions/7133676/generate-alphanumeric-strings-sequentially</p>

<br>

<p>2. Try each possible password combination using a for loop to go through our password list and make a post request using the useranme and possible password to the server using the requests library</p>

<p>Link to the requests documentation: http://docs.python-requests.org/en/master/</p>

<p>Hint 200 is a success and 400 is a failed login attempt: https://http.cat/</p>


## Resources for teachers
<p>The server code is a Node Express App which can be found in the server folder.</p>

<p>An example of how to generate all possible password combinations using sequential string generation can be found in the 'cracker' folder.</p>

<p>An example of how to send the requests to the server can be found in the 'sending' folder.</p>

<p>An example of how to send the requests to the server with the cracker code can be found in the 'example' folder.</p>

<p>The username is "mike" the password is "du42"</p>
