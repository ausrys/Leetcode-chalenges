function findKthLargest(nums, k) {
    function partition(left, right, pivotIndex) {
        const pivot = nums[pivotIndex];
        [nums[pivotIndex], nums[right]] = [nums[right], nums[pivotIndex]]; // Move pivot to end
        let storeIndex = left;

        for (let i = left; i < right; i++) {
            if (nums[i] > pivot) { // > for kth largest
                [nums[i], nums[storeIndex]] = [nums[storeIndex], nums[i]];
                storeIndex++;
            }
        }

        [nums[storeIndex], nums[right]] = [nums[right], nums[storeIndex]]; // Move pivot to final place
        return storeIndex;
    }

    let left = 0, right = nums.length - 1;
    const target = k - 1;

    while (left <= right) {
        const pivotIndex = left + Math.floor(Math.random() * (right - left + 1));
        const index = partition(left, right, pivotIndex);

        if (index === target) {
            return nums[index];
        } else if (index < target) {
            left = index + 1;
        } else {
            right = index - 1;
        }
    }
}
