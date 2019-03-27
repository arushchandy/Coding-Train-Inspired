var Tree = function() {
  this.root = null;
};

Tree.prototype.addValue = function(n) {
  var v = new Node(n);
  if (this.root == null) {
    this.root = v;
  } else {
    this.root.addNode(v);
  }
};
