# R language

The R-language has a steep learning curve, so focus and pay attention. Its is a specialised language created for Data Analysis and Statistical Predictive Modeling. Google recommended.

## R-Framework and R-Studio

[R Framework](https://cloud.r-project.org)
[R Studio](https://www.rstudio.com/products/rstudio/#rstudio-desktop)

## Install R and R-Studio

Installers are available for all popular Operating Systems in the above links. Download and install with default settings.

## R-Programming

### Data Types

#### Integer
"L" denotes that R should store variable as an integer. By default all numbers are stored as a double.
x <- 2L
typeof(x)

#### Double

d <- 10.25
typeof(d)

#### Complex Number

c <- 5 + 6i
typeof(c)

#### Character

a <- "Hello"
typeof(a)

#### Logical

t <- T or TRUE
f <- F or FALSE

### Working with variables

num1 <- 10L
num2 <- 11.5
total <- num1 + num2
total

#### Call built-in Function

num3 <- 25
sqrt(num3)

greet <- "Hello"
contact <- 'Bob'
paste(greet, contact)

#### Comparison Operators

== != < > <= >= ! | & isTRUE(x)

value = 10 > 9
typeof(value)

``` r
# AND
3 > 4 & 4 < 5
# OR
3 > 4 | 4 < 5
```

#### Loops

While loop
``` r
# Loop 10 times
counter <- 0
while(counter < 10){
  print(counter)
  counter <- counter + 1
}
```

For loop
``` r
# Loop 10 times
range = 0:9
for (counter in range) {
  print(counter)
}
```

#### if ... else if ... else statement

``` r
condition <- 1 > 2
if(condition) {
  print("Condition is true")
}else {
  print("Condition is false")
}

# Remove variable from environment
rm(value)
# Random Number
value <- rnorm(1)
print(value)
if(value >= 1) {
  print("More than equal to 1")
}else if (value < 1 & value > -1) {
  print("Almost Zero")
} else if (value <= -1) {
  print("Less than equal to -1")
}
```

