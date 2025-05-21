var containsNearbyDuplicate = function (nums, k) {
  let index_num = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (index_num.has(nums[i]) && i - index_num.get(nums[i]) <= k) return true;
    index_num.set(nums[i], i);
  }
  return false;
};

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
