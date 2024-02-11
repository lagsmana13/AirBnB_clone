# AirBnB Clone - The Console

Welcome to the AirBnB clone project! This project aims to build a command-line interface (CLI) that allows users to manage AirBnB objects. It serves as the first step towards building a full web application by providing the foundation for subsequent projects, such as HTML/CSS templating, database storage, API development, and front-end integration.

## Command Interpreter

The command interpreter is a CLI tool that enables users to interact with the AirBnB objects through a set of commands. It provides functionality for creating, updating, deleting, and querying AirBnB objects. The command interpreter also supports serialization and deserialization of instances to and from various formats, including dictionaries and JSON strings.

### Starting the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open a terminal or command prompt in the project directory.

Run the following command to start the command interpreter:

```
$ ./console.py
```

### Using the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- **create**: Create a new instance of an AirBnB object.
  ```
  (hbnb) create <class_name>
  ```
  Example: `create User`

- **show**: Display information about a specific instance of an AirBnB object.
  ```
  (hbnb) show <class_name> <object_id>
  ```
  Example: `show User 123`

- **update**: Update attributes of a specific instance of an AirBnB object.
  ```
  (hbnb) update <class_name> <object_id> <attribute_name> "<attribute_value>"
  ```
  Example: `update User 123 name "John Doe"`

- **destroy**: Delete a specific instance of an AirBnB object.
  ```
  (hbnb) destroy <class_name> <object_id>
  ```
  Example: `destroy User 123`

- **all**: Display information about all instances of AirBnB objects or all instances of a specific class.
  ```
  (hbnb) all
  ```
  Example: `all` or `all User`

- **quit**: Exit the command interpreter.
  ```
  (hbnb) quit
  ```

### Examples

Here are some examples of how to use the command interpreter:

- Creating a new User instance:
  ```
  (hbnb) create User
  ```

- Updating the name attribute of a User instance:
  ```
  (hbnb) update User 123 name "John Doe"
  ```

- Displaying information about all instances of User:
  ```
  (hbnb) all User
  ```

## Authors


BY Hamdi Khalil