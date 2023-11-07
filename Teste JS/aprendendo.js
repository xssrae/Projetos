//Números pares e impares

function EvenValues(array){
    let evenNums = [];
    for(let i=0; i < array.length; i++ ){
        if (array[i] % 2 == 0 ) {
            evenNums.push(array[i]);  
        }
        else{
            console.log(`${array[i]} não é par!`)
        }
    }
    console.log(evenNums)
}

let array = [1, 2, 4, 8, 16]

EvenValues('Os números pares são: ',array)