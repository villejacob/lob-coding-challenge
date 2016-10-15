# Jacob Ville
## Lob Coding Challenge


## Summary
This project is a website using Flask, that collects user information through
an HTML form, and opens a pdf of a letter to their governor using the provided
information. A link to this pdf URL is also printed to the terminal.


### Required modules
The following modules are used:

Install each using pip:

- 'pip install requests'
- 'pip install lob'
- 'pip install webbrowser'
- 'pip install random'
- 'pip install threading'
- 'pip install flask'

### Project files and folder layout
- Ville Lob Coding Challenge
    - static  
        - 'ville\_style.css'
    - templates  
        - ville\_index.html'
    - 'ville\_api\_keys.py'
    - 'ville\_communicate.py'
    - 'README.md'

### Input
The user inputs their name, address, and letter content within the webpage. <br>

### Output
Once the user fills out their information, an error will prompt them if any
required information was omitted. Once all information is filled out, a new
window will open, presenting the pdf of their letter to their governor.
A link to this URL is also printed to the terminal.  <br>

### Make the magic happen (run the project)
Once all modules are installed, navigate to the folder "Ville Lob Coding Challenge"
within the terminal. Use the command 'python ville_communicate.py' and voila, the
website should open in the default web browser.

Enter address and letter iformation, then press 'get letter' to open the pdf in a new tab.
If greeted by an unfriendly page with lots of angle brackets and an XML warning, just refresh the page.
Otherwise, enjoy talking at your governor!<br>

##### _Thanks for your consideration! I hope you enjoy reviewing this as much as I enjoyed making it,_
*Jacob Ville*
