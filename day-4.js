// https://chatgpt.com/c/693282ce-e678-832b-9799-9a2af4d079d7




// ----- Example -----

// Fixed-size window example: max sum of any 3 consecutive numbers
function maxSumFixedWindow(arr, k) {
    let windowSum = 0;
    for (let i = 0; i < k; i++) windowSum += arr[i];   // build first window
    let maxSum = windowSum;
    // console.log("maxSum",maxSum)
    for (let i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];  // slide: add new, remove old
        maxSum = Math.max(maxSum, windowSum);
        // console.log(maxSum)
    }
    return maxSum;
}


console.log(maxSumFixedWindow([1,2,3,4,5],1))



// Day 4

// 1. Warm-up — Max Sum Subarray of Size K


// function maxSumofSubArray(arr,k){
//     let windowSum = 0 
//     for(let i = 0; i < k; i++) {
//         windowSum += arr[i]
//     }
//     let maxSum = windowSum;

//     for (let i = k; i < arr.length; i++) {
//         windowSum += arr[i] - arr[i - k];  // slide: add new, remove old
//         maxSum = Math.max(maxSum, windowSum);
//     }
//     return maxSum;
// }

// GPT Answer
function maxSumofSubArray(arr, k) {
  if (arr.length < k) return null;

  let windowSum = 0;

  // First window
  for (let i = 0; i < k; i++) {
    windowSum += arr[i];
  }

  let maxSum = windowSum;

  // Slide the window
  for (let i = k; i < arr.length; i++) {
    windowSum = windowSum - arr[i - k] + arr[i];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}

console.log(maxSumofSubArray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4));
// 24


function longestSubstring(str) {
    const seen = new Set();
    let left = 0;
    let maxLen = 0;

    for (let right = 0; right < str.length; right++) {
        
        while(seen.has(str[right])){
            seen.delete(str[left])
            left++
        }
        // while str[right] is already in `seen`:
        //     remove str[left] from seen
        //     move left forward by 1

        // add str[right] to seen
        seen.add(str[right])

        // update maxLen using (right - left + 1)
        maxLen = Math.max(maxLen,right - left + 1)
    }
    return maxLen;
}

console.log(longestSubstring("abcabcbb"))

// 3. Stretch — Smallest Subarray with Sum ≥ Target

function smallestSubArraySum(arr, target) {
    let left = 0;
    let sum = 0;
    let minLen = Infinity;

    for (let right = 0; right < arr.length; right++) {
        // add arr[right] to sum
        sum +=arr[right]

        // while sum >= target:
        //     update minLen if (right - left + 1) is smaller
        //     subtract arr[left] from sum
        //     move left forward by 1
        
        while (sum >= target){
            minLen = Math.min(minLen,right - left + 1)
            sum -= arr[left];
            left++
        }
    }

    return minLen === Infinity ? 0 : minLen; // (handle the case where no valid window was found)
}

console.log(smallestSubArraySum([2, 5, 2, 3, 2],7))

