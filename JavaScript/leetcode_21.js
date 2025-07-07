function ListNode(val, next) {
<<<<<<< HEAD
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var mergeTwoLists = function (list1, list2) {
  let dummy = new ListNode();
  let current = dummy;
  while (list1 && list2) {
    if (list1.val < list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }
  current.next = list1 ? list1 : list2;
  return dummy.next;
=======
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

var mergeTwoLists = function (list1, list2) {
    let dummy = new ListNode();
    let current = dummy;
    while (list1 && list2) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    current.next = list1 ? list1 : list2;
    return dummy.next;
>>>>>>> a240f511499660ef602885c94b58faa12d2f12e8
};
