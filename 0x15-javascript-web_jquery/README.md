# 0x15 - JavaScript

## Resources
### Read or watch:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner](https://flukeout.github.io/) Play with Selectors
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
    - [Introduction to web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
    - [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
    - [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)


## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General 
- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

## Requirements
### General
- Allowed editors: All of them.
- All your files will be interpreted on Chrome browser (version 57.0 or later)
- All your files should end with a new line
- A mandatory `README.md` file with meaningful information about the content, should be placed at the root folder of the project.
- Your code should be `semistandard` compliant
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## Tasks

### 0. No JQuery
- Level: 0
- Manual review

Write a JavaScript script that updates the text color of the `header` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `0-script.js`
- Code language: `JavaScript` (project based)

### 1. Click and turn red
- Level: 0
- Manual review

Write a JavaScript script that updates the text color of the `header` element to red (`#FF0000`) when the user clicks on the tag with id `red_header`:

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `1-script.js`
- Code language: `JavaScript` (project based)

### 2. Add `.red` class
- Level: 0
- Manual review

Write a JavaScript script that adds the class `red` to the `header` element when the user clicks on the tag with id `red_header`

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `2-script.js`
- Code language: `JavaScript` (project based)

### 3. Toggle classes
- Level: 0
- Manual review

Write a JavaScript script that toggles the class of the `header` element when the user clicks on the tag id `toggle_header`:

The `header` element must always have one class: `red` or `green`, never both in the same time and never empty.
If the current class is `red`, when the user click on id `toggle_header` element, the class must be updated to `green` ; and the reverse.

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `4-script.js`
- Code language: `JavaScript` (project based)

### 4. List of elements
- Level: 0
- Manual review

Write a JavaScript script that adds a `li` element to a list when the user clicks on the element with id `add_item`:

The new element must be: `<li>Item</li>`
The new element must be added to the `ul` element with class `my_list`

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `4-script.js`
- Code language: `JavaScript` (project based)

### 5. Change the text
- Level: 0
- Manual review

Write a JavaScript script that updates the text of the `header` element to `New Header!!!` when the user clicks on the element with id `update_header`

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `5-script.js`
- Code language: `JavaScript` (project based)

### 6. Star wars character
- Level: 0
- Manual review
Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- The name must be displayed in the HTML tag with id `character`.
- You must use the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). 
- You probably should read something about [usign Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) later.

Please test with this HTML file in your browser:
```
javiercito@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `6-script.js`
- Code language: `JavaScript` (project based)

### 7. Star Wars movies
- Level: 0
- Manual review

Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be list in the HTML `ul` element with id `list_movies`
- You must use the Fetch API.

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/0x15$ 
```

#### Repo:

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `0x15-javascript-web_jquery`
- File: `7-script.js`
- Code language: `JavaScript` (project based)