# Word counts in CAMENA

Though scholars in the original project do not mention this anywhere, it seems that CAMENA contains a surprisingly large number of words -- about 50 million of them. Since most of the words are Latin, this is very important (for example, the collection Croatiae auctores in lingua Latina contains 5 million words).

We checked the number of words by turning CAMENA XML texts into a BaseX database and counting words (tokens) with two XQuery scripts. The first one counts all tokens in the database:

```XQuery

let $counts :=
for $w in ft:tokens("camena-neolatinlit")
let $n := number($w//@count)
return $n
return sum($counts)

```

This query returns **5.0753733E7**, that is **50,753,733** tokens.

The second XQuery script counts only the tokens below the `text` element:

```XQuery

let $counts :=
for $w in collection("camena-neolatinlit")//*:text
let $n := tokenize($w)
return count($n)
return sum($counts)

```

This query returns **50,458,045** tokens.


