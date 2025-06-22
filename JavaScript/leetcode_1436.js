/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    let pset = new Set();
    for (let index = 0; index < paths.length; index++) {
        pset.add(paths[index][0])
    }
    for (let index = 0; index < paths.length; index++) {
        if (!pset.has(paths[index][1])) return paths[index][1]
    }
};