extern crate num;

use num::{pow, FromPrimitive, ToPrimitive};
use num::bigint::BigInt;
use num::bigint::ToBigInt;

fn test_equation(x: BigInt) -> BigInt {
    pow(x.clone(), 2) + x + 1.to_bigint().unwrap()
}

fn my_equation(x: BigInt) -> BigInt {
    pow(x.clone(), 3) - (3.to_bigint().unwrap() * x) + 4.to_bigint().unwrap()
}

fn is_quadratic_residue(q: BigInt, p: BigInt) -> BigInt {
    let exp = (p.clone() - 1.to_bigint().unwrap()) / 2.to_bigint().unwrap();
    let r = pow(q, exp.to_usize().unwrap()) % p;
    println!("qr: {}", r); r
}

fn is_y_quadratic_residue(q: BigInt, p: BigInt) -> BigInt {
    let exp = (p.clone() + 1.to_bigint().unwrap()) / 4.to_bigint().unwrap();
    let r = pow(q, exp.to_usize().unwrap()) % p;
    println!("y: {}", r); r
}

fn main() {
    let p = 23.to_bigint().unwrap();
    for x in (0..22) {
        println!("Value for x: ")
        let y_2 = test_equation(x.to_bigint().unwrap());
        is_quadratic_residue(y_2.clone(), p.clone());
        is_y_quadratic_residue(y_2, p.clone());
    }
}
