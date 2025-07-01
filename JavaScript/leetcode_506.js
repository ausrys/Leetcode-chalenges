var findRelativeRanks = function (score) {
    const rankList = ["Gold Medal", "Silver Medal", "Bronze Medal"];

    // Create an array of [index, score] pairs
    const indexedScores = score.map((val, idx) => [idx, val]);

    // Sort descending by score
    indexedScores.sort((a, b) => b[1] - a[1]);

    // Prepare result array
    const result = new Array(score.length);

    // Assign ranks and medals
    for (let i = 0; i < indexedScores.length; i++) {
        const index = indexedScores[i][0];
        if (i < 3) {
            result[index] = rankList[i];
        } else {
            result[index] = (i + 1).toString();
        }
    }

    return result;
};
