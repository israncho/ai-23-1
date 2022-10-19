# Practice-01 Search algorithms

We provide an implementation of the Depth-First Search
algorithm applied to the 8-puzzle.

## To run the program

While in `practice01` folder run: 

```shell
python3 src/DFS.py '[[1,"e",2],[6,3,4],[7,5,8]]'
```

The list is the representation of the board,
you can check with a faster example

```shell
python3 src/DFS.py '[[1,2,3],[4,5,6],["e",7,8]]'
```

There are boards that have no solution
An example of this is the next representation of the board

```shell
python3 DFS.py '[[8,1,2],["e",4,3], [7,6,5]]'
```


### Tests

To execute the unit tests for the State class, run the following comand
while in the `practice01` folder.

```shell
python3 src/StateUnitTest.py
``` 

⌨️ with much :purple_heart: by [israncho](https://github.com/israncho) 😊⌨️,  [jose-mpm](https://github.com/Jose-MPM) 😊⌨️,  [ruben](https://github.com/Jose-MPM) 😊⌨️,  [Erick](https://github.com/Jose-MPM) 😊⌨️	