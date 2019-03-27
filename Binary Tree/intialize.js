var tree = new Tree();

(function() {
  // for (var i = 0; i < 100; i++) {
  //   var min = 4;
  //   var max = 5;
  //   var random = Math.random() * (+max - +min) + +min;
  //   var intVal = Math.floor(random);
  //   tree.addValue(intVal);
  // }
  tree.addValue(5);
  tree.addValue(4);
  tree.addValue(6);
  tree.addValue(15);
  tree.addValue(35);
  tree.addValue(1);
  console.log(tree);
  tree.traverse();
  tree.search(14);
})();
