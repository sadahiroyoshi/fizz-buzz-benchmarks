// ==ClosureCompiler==
// @output_file_name fizz_buzz_increment_compiled.js
// @compilation_level ADVANCED_OPTIMIZATIONS
// ==/ClosureCompiler==

var n = process.argv[2];
var fizzbuzz = 0;
var fizz = 0;
var buzz = 0;
var none = 0;
// const startTime = Date.now();
for(i=1; i<=n; i++){
    if(i%15 === 0){
        fizzbuzz++;
    }else if(i%3 === 0){
        fizz++;
    }else if(i%5 === 0){
        buzz++;
    }else{
        none++;
    }
}
// const endTime = Date.now();
// console.log("elapsed_time:"+(endTime - startTime)/1000+"[sec]");
console.log("fizzbuzz:"+fizzbuzz);
console.log("fizz:"+fizz);
console.log("buzz:"+buzz);
console.log("none:"+none);
