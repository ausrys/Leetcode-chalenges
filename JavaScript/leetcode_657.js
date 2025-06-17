/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let h = 0;
    let v =0;
    for (let index = 0; index < moves.length; index++) {
        switch (moves[index]) {
            case "U":
                h++
                break;
            case "D":
                h--
                break;
            case "L":
                v--
                break;
            default:
                v++
                break;
        }; 
    };
    return v === 0 && h === 0
};