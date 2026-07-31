// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

console.log("Start small. Ship something.");

// 1. Warm-up — Reverse a String

function reverseString(str){
    let reverstr = ""
    for(let i = str.length-1; i >= 0; i--){
        reverstr += str[i]
    }
    
    // for(let i = 0 ; i < str.length; i++){
    //     reverstr += str[(str.length-1) + i]
    // }
    
    return reverstr
}

console.log(reverseString("hello"))

// 2. Core — Count Vowels

function countVowels(str){
    const vowels = ["a","e","i","o","u"]
    let count = 0;
    for(item of str.toLowerCase()){
        if(vowels.includes(item)){
            count += 1
        }
    }
    return count
}

console.log(countVowels("Programming"))

// 3. Stretch — First Non-Repeating Character
function nonRepeateChar(str){
    const countRepeatChar = {}
    for(let i = 0; i < str.length; i++){
        
        if(str[i] in countRepeatChar) {
            countRepeatChar[str[i]] += 1
        } else {
            countRepeatChar[str[i]] = 1
        }
    
    }
    for(let i = 0; i < str.length; i++) {
        if(countRepeatChar[str[i]] ===1) return str[i]
    }
    // return [...str].filter(c=>str.indexOf(c) === str.lastIndexOf(c))[0]
}

console.log(nonRepeateChar("swiss"))
