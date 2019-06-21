## UwU Wat is dis?
Lng Language.

___wha...___

An esolang.

___what kind?___

Shorter syntax one.

___....___

This thing are using SLY so its need python 3.6 or greater.
As how to install SLY itself, just type ```pip install sly``` on your terminal/cmd

___...ok. What this thing could do?___

Just like ~~my friends~~ similar esolang, this one could print, do calculation (only in REAL INTEGER. I REPEAT. ONLY IN REAL INTEGER ~~FAILED TO DO SO WOULD CAUSE YOUR PC TO BLUESCREEN!! jk~~), assign variabel, for loop, comment the code, and create a function using those command above.

___I see... then, how do I run it?___

Easy way... just run it!

Or, follow dis steps if you don't know what to do:
1. Open ye terminal/cmd.
2. Change the dir to where ya extract dis lang.
3. run the lng.py.
4. ....
5. PROFIT???

Don't know how to run python file? geez...
Here, copypasta this line to your terminal.
```
python lng.py
```

BTW, you could ask it to read the code that you write on the other file (with this Lng language, duh).

i.e. like this...
```
python lng.py ini.text
```

___Wait... it use ".text" extention?___

Nope, it doesn't have to ".text", it could whatever you want to!! _~~even file without extention~~_.

What? Don't belive me? Suit yourself...

# Documentation
## Commands used on Lng language
### Print HelloWorld!!
**ex:**
```
P "HelloWorld!!" 
```
**result**
```
HelloWorld!!
```
**or:**
```
a= "Hello World!!"
P a
```
**result**
```
"Hello World!!"
```

### Calculation
**ex:**
```
1+2
4-3
3*1
4/2
```
**result**
```
3
1
3
2
```
**or**
```
a=3
b=2
P a+b
P a-b
P a*b
P a/b
```
**result**
```
5
1
6
1
```

___shouldn't 3 divided by 2 equals 1.5??___
LIKE I SAID BEFORE, THIS THING CAN __DO CALCULATION ON REAL INTEGER ONLY__ SO PLEASE EXPECT ITS OUTPUT TO BE __INTEGER__

### If else 
```
I expr TH true E false
```

**ex:**
```
a=1
n="meh"
I a==1 TH P "aye" E P n
```
**result**
```
aye
```

### for loop
```
F expr TO expr TH stmt
```

**ex:**
```
F i=0 T 5 TH P i
```
**result**
```
0
1
2
3
4
```

### Comment Usage
You can use '#' symbol to make comment in your source code.

**ex:**
```
a=1
n="meh" # I mean... you already figure out how its work, right?
I a==1 TH P "aye" E P n
```
**result**
```
aye
```

### Function
```
FN functionName() -> here's come your code...
```
then, you could just call the function
```
functionName()
```
like that...

**ex:**
```
FN yay() -> P "louder"
yay()
```
**result**
```
louder
```
**or**
```
FN wat() -> F x=0 TO 10 TH I x==5 TH x * 100 E x
wat()
```
**result**
```
0
1
2
3
4
500
6
7
8
9
```

...there, thats it all it can do.

___why are you made this?___

To ~~get gud grade~~ fullfil class final project.

# About
An esolang made ~~for fun~~ with my ~~fellow tennant~~ group using SLY(Sly Lex-Yacc) library to ~~accomplishly~~ fulfill our class final project.

## Our Group:
- Mahendra Adhi Prasetiya
- Indah Sekar Arum
- Dana Ramza Fahma