# simplate
Python Simple Templating

```
import Simplate
emailString = "Dear {name}, thank you for your {item}, unfortunately its sold, sincerely {author}."
emailTemplate = Simplate.Simplate(emailString, "EmailToCustomer")
emailToBob = emailTemplate.implement()
emailToBob.author = "Kyle Kimery"
emailToBob.name = "Bob"
emailToBob.item = "Weaboo Merchandise"
print emailToBob
```
```
Dear Bob, thank you for your inquiry regarding Weaboo Merchandise, I regret to inform you that it's gone, sincerely Kyle Kimery.
```