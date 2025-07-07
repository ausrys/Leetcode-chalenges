function isOneBitCharacter(bits) {
    let i = 0;
    while (i < bits.length - 1) {
        if (bits[i] === 1) {
            i += 2; // two-bit character
        } else {
            i += 1; // one-bit character
        }
    }
    return i === bits.length - 1;
}
