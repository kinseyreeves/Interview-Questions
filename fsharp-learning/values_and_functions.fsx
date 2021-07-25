let helloworld = printfn "hello world"



let addTwoNumbers x y = x + y

let add5ToNumber = addTwoNumbers 5

let out = add5ToNumber 10

let givemeathree x = 3



// Pattern matching


let rec fib n = 
    match n with
        | 0 -> 0
        | 1 -> 1
        | _ -> fib (n-1) + fib (n-2)
    
printfn "%d" (fib 2)

let rec factorial n =
    match n with
        | 0 | 1 -> 1
        | n -> n*factorial(n-1)


let sign = function
    | 0 -> 0
    | x when x < 0 -> -1
    | x when x > 0 -> 1

printfn "%d" (factorial 5)


printfn "%d" (sign 10)