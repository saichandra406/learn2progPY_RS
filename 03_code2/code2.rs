fn printTriangle(size: i32) -> i32 {
    //start with starCount being 0
    let mut starCount = 0;
    //count from 0 (inclusive) to size (exclusive), for each number i that you count
    for i in 0..size {
        //count from 0 (inclusive) to i (inclusive), for each number j that you count
        for j in 0..=i {
            //print a "*"
            print!("*");
            //increment starCount
            starCount += 1;
        }
        //when you finish counting on j,
        //print a newline ("\n")
        println!();
    }
    //when you finish counting on i, 
    //your answer is starCount
    starCount
}


fn main() {
    let mut numStars: i32;

    println!("Here is a triangle with height 4");
    numStars = printTriangle(4);
    println!("That triangle had {} total stars", numStars);

    //now print "Here is a triangle with height 7\n"
    println!("Here is a triangle with height 7");
    
    //then call printTriangle, passing in 7, and assign the result to numStars
    numStars = printTriangle(7);

    //finally, print "That triangle had %d total stars\n", such that the %d
    //prints the value of numStars
    println!("That triangle had {} total stars", numStars);
}