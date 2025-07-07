function subsets(nums) {
  const result = [];

<<<<<<< HEAD
  function backtrack(start, path) {
    result.push([...path]); // Add a copy of current subset

    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]); // Choose
      backtrack(i + 1, path); // Explore
      path.pop(); // Un-choose (backtrack)
=======
    function backtrack(start, path) {
        result.push([...path]); // Add a copy of current subset

        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]); // Choose
            backtrack(i + 1, path); // Explore
            path.pop(); // Un-choose (backtrack)
        }
>>>>>>> a240f511499660ef602885c94b58faa12d2f12e8
    }
  }

<<<<<<< HEAD
  backtrack(0, []);
  return result;
=======
    backtrack(0, []);
    return result;
>>>>>>> a240f511499660ef602885c94b58faa12d2f12e8
}
