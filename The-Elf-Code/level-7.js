var dist = 1
var move = [elf.moveDown, elf.moveLeft, elf.moveUp, elf.moveRight, elf.moveDown, elf.moveLeft, elf.moveUp, elf.moveRight];
for (var i = 0; i < 8; i++) {
  move[i](dist)
  elf.pull_lever(dist - 1)
  dist++
}
elf.moveUp(2)
elf.moveLeft(4)
function munch_ass(arr) {
  let add = arr.flat().reduce((sum, value) => (typeof value == "number" ? sum + value : sum), 0);
  return add
}
elf.tell_munch(munch_ass)
elf.moveUp(2)
