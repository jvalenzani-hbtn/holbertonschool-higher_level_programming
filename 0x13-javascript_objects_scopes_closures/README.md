# 0x13. JavaScript - Objects, Scopes and Closures

## Learning Objectives
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

## Install semi-standard
```bash
$ sudo npm install semistandard --global
```

## ES6 Compliant
To make the project ES6 compliant you must define the project as a module so it can be imported from the main files.  
Add a project.json like this.
```json
{
  "name": "0x13-javascript_objects_scopes_closures",
  "version": "1.0.0",
  "description": "## Learning Objectives - Why JavaScript programming is amazing - How to create an object in JavaScript - What this means - What undefined means - Why the variable type and scope is important - What is a closure - What is a prototype - How to inherit an object from another",
  "type" : "module",
  "directories": {
    "test": "test"
  }
}
```
