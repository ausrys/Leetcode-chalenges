/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
function shortestCompletingWord(licensePlate, words) {
  // Remove digits and spaces, and convert to lowercase
  const cleaned = licensePlate.toLowerCase().replace(/[^a-z]/g, '');
  
  // Count letters in licensePlate
  const getCharCount = (str) => {
    const count = {};
    for (const char of str) {
      count[char] = (count[char] || 0) + 1;
    }
    return count;
  };
  
  const mainCounter = getCharCount(cleaned);
  let result = null;

  for (const word of words) {
    const wordCounter = getCharCount(word);
    let isValid = true;
    
    for (const char in mainCounter) {
      if (!wordCounter[char] || wordCounter[char] < mainCounter[char]) {
        isValid = false;
        break;
      }
    }

    if (isValid && (result === null || word.length < result.length)) {
      result = word;
    }
  }

  return result;
}

console.log(shortestCompletingWord('12 asd4s 1e'));