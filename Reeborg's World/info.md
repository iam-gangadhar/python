### Website URL
```sh
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
```

#### Home 1 code
```sh
def turn_around():
    turn_left()
    turn_left() 
move()
move()
turn_around()
```
### Home 2 code
```sh
move()
move()
```
### Home 3 code
```sh
move()
move()
turn_left()
move()
```
#### Home 4 Code
```sh
def turn_around():
    turn_left()
    turn_left()
 
def jump():
    move()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_left()
    
move()
move()
move()
turn_left()
jump()
jump()
jump()
move()
move()
move()
```
#### Hurdle 1 & 2 can be work in same Code
```sh
def turn_around():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
x = True
while x:
    if at_goal():
        x = False
    else:
        jump()
```
#### Hurdle 3 Code
```sh
def turn_around():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
    
x = True
while x:
    if at_goal():
        x = False
    elif wall_in_front():
        turn_left()
        jump()
    else:
        move()
```
  