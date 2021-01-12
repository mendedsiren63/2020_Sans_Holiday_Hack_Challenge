for (var i = 0; i < 4; i++) {
  elf.moveTo(lollipop[i])
}
elf.moveTo(lever[0])
var new_arr = ["munchkins rule"]
var add = new_arr.concat(elf.get_lever(0))
elf.pull_lever(add)
elf.moveTo(munchkin[0])
elf.moveUp(2)
