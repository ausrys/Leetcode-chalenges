/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    let fives = 0;
    let tens = 0;
    for (let index = 0; index < bills.length; index++) {
        if (bills[index] === 5) fives++;
        else if (bills[index] ===10) {
            fives--;
            tens++;
        }
        else {
            if(tens >= 1) {
                fives--;
                tens--;
            }
            else fives -= 3;
        }
        if (fives < 0) return false;
    }
    return true;
};