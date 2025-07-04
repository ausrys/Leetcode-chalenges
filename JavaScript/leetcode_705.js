var MyHashSet = function () {
    this.size = 1000;
    this.buckets = Array.from({ length: this.size }, () => []);
};

// Simple hash function
MyHashSet.prototype._hash = function (key) {
    return key % this.size;
};

MyHashSet.prototype.add = function (key) {
    const index = this._hash(key);
    const bucket = this.buckets[index];
    if (!bucket.includes(key)) {
        bucket.push(key);
    }
};

MyHashSet.prototype.remove = function (key) {
    const index = this._hash(key);
    const bucket = this.buckets[index];
    const keyIndex = bucket.indexOf(key);
    if (keyIndex !== -1) {
        bucket.splice(keyIndex, 1);
    }
};

MyHashSet.prototype.contains = function (key) {
    const index = this._hash(key);
    const bucket = this.buckets[index];
    return bucket.includes(key);
};
