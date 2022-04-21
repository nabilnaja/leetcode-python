#### 22. Generate Parentheses

* Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

* Complexity analysis

Time complexity: O( n * 4^n / (n * n^(1/2)))->  O( 4^n / n^(1/2)).

The first n is here because we have to copy this combination to result array. 

The 4^n / (n * n^(1/2)) is the n-th Catalan number

Space complexity: O( 4^n / n^(1/2)).

* keyword : backtracking Catalan-number