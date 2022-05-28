var sortColors = function (nums) {
  function swap(i, j) {
    [nums[i], nums[j]] = [nums[j], nums[i]];
  }
  let left = 0,
    right = nums.length - 1,
    mid = 0;
  while (mid <= right) {
    if (nums[mid] == 0) {
      swap(mid, left);
      left++;
      mid++;
    } else if (nums[mid] == 2) {
      swap(mid, right);
      right--;
    } else {
      mid++;
    }
  }
};

console.log(sortColors([2, 0, 2, 1, 1, 0]));
