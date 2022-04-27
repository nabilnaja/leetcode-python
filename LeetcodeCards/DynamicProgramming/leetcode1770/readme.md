#### 1770. Maximum Score from Performing Multiplication Operations

* Description

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are
1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score. Remove x from the array nums.
Return the maximum score after performing m operations.

* Complexity analysis bottom-up

Time complexity: .

Space complexity: .

* Complexity analysis top-down

Time complexity: .

Space complexity: .

* keyword : dynamic-programming-card