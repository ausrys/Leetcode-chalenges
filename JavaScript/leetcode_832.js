/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    const replacements = new Map([[1, 0], [0,1]]);
    for (let index = 0; index < image.length; index++) {
        image[index].reverse();
        for (let j = 0; j < image[index].length; j++) {
            image[index][j] = replacements.get(image[index][j])
        };
    };
    return image;
};

console.log(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]));