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
  } else if (n.value > this.value) {
    if (this.right == null) {
      this.right = n;
    } else {
      this.right.addNode(n);
    }
  }
};

Node.prototype.visit = function() {
  if (this.left != null) {
    this.left.visit();
  }
  console.log(this.value);
  if (this.right != null) {
    this.right.visit();
  }
};

Node.prototype.search = function(n) {
  if (this.value == n) {
    return this;
  }
  if (this.value > n && this.left != null) {
    return this.left.search(n);
  }

  if (this.value < n && this.right != null) {
    return this.right.search(n);
  }

  return null;
};
