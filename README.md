# Stock
Check stock for an online store using the existence of their common phrase (e.g., "out of stock")

This file was originally developed for a Macbook. At the start of the quarantine, gyms were closed and home equipment was out of stock everywhere. I taught myself about the basics of web scraping and wrote this program in Python. And I did purchase some awesome dumbbells the moment they were in stock again!


**Purpose:** 
Scrape the identified website for the *indicator/phrase* that marks an item as "out of stock". When the *indicator/phrase* is missing, the program emails an alert to the user.


**Steps:**
1. Answer prompts for URL, website's phrase for "out of stock", email details
    - *Regular email password might not work because of domain security; user may need to generate an app password, as shown in gmail instructions here: [Sign In with App Passwords](https://support.google.com/accounts/answer/185833?hl=en).*
2. Program checks URL for "out of stock" (or other phrasing)

3. If "out of stock" is found (i.e., item **is** "out of stock"), program waits 1 hour to check stock again
    - *To reassure that the program is still functioning, "Running" will print on the screen every 10 minutes between checks*

4. When "out of stock" is not found (i.e., item is listed in stock), program prints a confirmation message and emails an alert to the address provided in step 1


**Future Developments:**
Future enhancements will include...
- [ ] Import OS package to check the user's operating system
    - *The current code was intended for hobby use on a Macbook, and certain lines will not function on other operating systems (OS) (e.g., Windows).*
    - *Importing the OS package will allow the program to see which OS the user has and operate the proper code respective to it*

- [ ] Import tkinter
    - *I'd like to dabble in a friendlier user interface, which would require use of tkinter*
