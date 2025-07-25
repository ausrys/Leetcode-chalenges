/* 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/

var climbStairs = function (n) {
    if (n <= 1) return 1;
    let a = 1;
    let b = 1;
    for (let index = 2; index < n + 1; index++) {
        [a, b] = [b, a + b];
    }
    return b;
};

console.log(climbStairs(5));
