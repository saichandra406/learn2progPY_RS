fn max(num1: i32, num2: i32) -> i32 {
    if(num1 > num2) {
        num1
    } else {
        num2
    }
}

#[allow(overflowing_literals)]
fn main() {
    println!("max(42, -69) is {}", max(42, -69));
    println!("max(33, 0) is {}", max(33, 0));
    println!("max(0x123456, 123456) is {}", max(0x123456, 123456));
    //compute the max of 0x451215AF and 0x913591AF and print it out as a decimal number
    println!("max(0x451215AF, 0x913591AF)is {}", max(0x451215AF, 0x913591AF));
}