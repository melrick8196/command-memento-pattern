# CS635-Assignment3

Memento pattern, command pattern and decorator pattern

Q) Instead of creating decorator(s) you might be tempted to make the Inventory class create 
the commands, execute the commands and save them. Why is the decorator a better idea.

>> Decorators help in giving the object more power. If the parent class is to be 
>modified in the future, instead of modifying the whole class and changing
>its data and operations we can decorate the class with those modifications
>and thus avoid class explosion.