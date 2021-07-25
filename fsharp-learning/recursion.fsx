open System

let rec factorial n =
    match n with
        | x when x < 0 -> -1
        | 0 -> 1
        | _ -> n*factorial(n-1)


printfn "%d" (factorial -1)

Console.WriteLine(factorial 10)


//Greatest common denominator
let rec gcd x y = 
    if y = 0 then x
    else gcd y (x % y)


//Console.WriteLine(gcd 259 111)

let rec multiply x y =
    if y > 1 then 
        x + (multiply x (y-1))
    else x

//Console.WriteLine(multiply 10 5)

let tailRecMultiply x y =
    let rec loop acc counter =
        if counter > 1 then 
            loop (acc+x) (counter-1)
        else acc
    loop x y

Console.WriteLine(tailRecMultiply 10 5)