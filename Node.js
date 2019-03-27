var Node = function(val) {
  this.left = null;
  this.right = null;
  this.value = val;
};

Node.prototype.addNode = function(n) {
  if (n.value < this.value) {
    if (this.left == null) {
      this.left = n;
    } else {
      this.left.addNode(n);
    }
  } else {
    if (this.right == null) {
      this.right = n;
    } else {
      this.right.addNode(n);
    }
  }
};
