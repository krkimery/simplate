# Simplate
Python Simple Object-Based String Templating

## Usage
From formatted strings create re-usable template objects and implementation objects. The Simplate class (Simplate.Simplate)
allows you to dynamically create new Template classes with the string you initialize with, and (optionally) a title
for the template which becomes the name of your new class. 

```
import Simplate

mySimpleTemplate = Simplate.Simplate( "Hello {friend} how's your {pet}?", title="FriendlyLetter" )
print mySimpleTemplate.ImplementationClass
```
```
<class 'Simplate.Simplate.FriendlyLetter'>
```
```
newLetterToJohn = mySimpleTemplate.implement()
type(newLetterToJohn)
```
```
<class 'Simplate.Simplate.FriendlyLetter'>
```
```
newLetterToJohn.friend = "John"
newLetterToJohn.pet = "cute puppy"
str(newLetterToJohn)
```
```
"Hello John how's your cute puppy?"
```

Every call to Simplate.implement() will return a new instance of the dynamically-created template class, and the parameters
on the template string become the instance variables on the new instances of this new template class, while the template
itself is a shared class variable amongst all instances of this template. 

An optional third argument when initializing a Simplate is "defaults", which is what the default values are for the instance
variables of the template object. By default, defaults is an empty string.

## Examples
```
import Simplate
emailString = "Dear {name}, thank you for your {item}, unfortunately its sold, sincerely {author}."
emailTemplate = Simplate.Simplate(emailString, "EmailToCustomer")
emailToBob = emailTemplate.implement()
emailToBob.author = "Kyle Kimery"
emailToBob.name = "Bob"
emailToBob.item = "Baseball Merchandise"
print emailToBob
```
```
Dear Bob, thank you for your inquiry regarding Baseball Merchandise, I regret to inform you that it's gone, sincerely Kyle Kimery.
```