#!/usr/bin/node
if(isNaN(size)) {
  console.log('Missing size')
}
for (let i = 0; i < process.argv[2]; i++) {
    console.log('x');
    for (let y = 0; y < process.argv[2]; y++) {
        console.log('x');
    }
  }