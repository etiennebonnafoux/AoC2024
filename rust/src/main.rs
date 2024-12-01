use std::fs;

fn main() {
let mut content = String::new();
content = fs::read_to_string("input_jour_un.txt").expect("Failed to read file");
println!("{}",content)
}

