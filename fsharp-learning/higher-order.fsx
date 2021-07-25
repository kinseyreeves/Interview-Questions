open System

let b = 20

let map x f = f x

let square x = x * x

let cubeAndConvertToString x =
    let temp = x * x * x
    temp.ToString()
    
let answer x =
    if x = true then "yes"
    else "no"

let first = map 5 square
let second = map 5 cubeAndConvertToString
let third = map true answer

let add x y= x+y

let toString x = x.ToString()

let complexFunction x =
    toString (add 5(square x))

let complexFunction2 x =
    x|> square |> add 5 |> toString


