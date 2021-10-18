// ==ClosureCompiler==
// @output_file_name fizz_buzz_println_compiled.js
// @compilation_level ADVANCED_OPTIMIZATIONS
// ==/ClosureCompiler==

var n = process.argv[2];
// const startTime = Date.now();
for(i=1; i<=n; i++){
    if(i%15 === 0){
        console.log("fizzbuzz");
    }else if(i%3 === 0){
        console.log("fizz");
    }else if(i%5 === 0){
        console.log("buzz");
    }else{
        console.log(i);
    }
}
// const endTime = Date.now();
// console.log("elapsed_time:"+(endTime - startTime)/1000+"[sec]");
