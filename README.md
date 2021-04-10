# lambda-calculus-translation-kylan

Write a compiler that accepts terms in the lambda calculus and outputs either JavaScript or Python or (massively harder) C.

Here’s the grammar of the input language:

```
  LC	 	=	 	num
 	 	|	 	id
 	 	|	 	(/ id => LC)
 	 	|	 	(LC LC)
 	 	|	 	(+ LC LC)
 	 	|	 	(* LC LC)
 	 	|	 	(ifleq0 LC LC LC)
 	 	|	 	(println LC)
```

... where num is a number, and id is an identifier.
