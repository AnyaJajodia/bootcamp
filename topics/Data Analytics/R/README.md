# R language

The R-language has a steep learning curve, so focus and pay attention. Its is a specialised language created for Data Analysis and Statistical Predictive Modeling. Google recommended.

## R-Framework with R-Studio

[R Framework](https://cloud.r-project.org)
[R Studio](https://www.rstudio.com/products/rstudio/#rstudio-desktop)

## Install R and R-Studio

Installers are available for all popular Operating Systems in the above links. Download and install with default settings.

## R-Programming

"<-" is assignment operator, equivalent to "=" in most other languages.
NA is not-assigned or not-available, equivalent to None in other languages.
"?func" will display help for that function.

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
# Random Number, normal deviation -3 to +3
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


### Exercise - Coin Toss probability validation

The Law of Large Numbers theorizes that the average of a large number of results closely mirrors the expected value, and that difference narrows as more results are introduced.

Statistics Terms:

1. mean or average = sum of all values divided by total number of values

2. median = the value separating the higher half from the lower half of a data sample, it may be thought of as "the middle" value

3. standard deviation = how far on average the values differ from the mean, high deviation is for values far away from mean and low deviation is when values are clustered close to the mean

4. normal distribution = Normal Distribution has a bell shape, the mean and median are equal, and 68% of the data falls within 1 standard deviation. ![Normal Distribution Image](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/2560px-Standard_deviation_diagram.svg.png)


Exercise:
Apply Law of Large Numbers to a series of coin tosses. So as the sample size increases the average value (mean) moves closer to the probable/expected value of 50%.

``` r
count <- 10000
counter <- 0
# heads
for(i in rnorm(count)){
  if (i > 0) {
    counter <- counter + 1
  }
}

average = counter / count
print(paste(count, counter, average*100, "%"))
```

### Vectors

A vector is a sequence of elements

Numeric vector
Character vector

Vectors can only contain elements of the same type either number (integer or double) or character not mixed.
All numbers are vectors os length 1

``` r
# Combine function
my_vector <- c(1,2,3,4,5)
print(my_vector)
is.numeric(my_vector)
is.integer(my_vector)
is.double(my_vector)
is.character(my_vector)

# Integers are converted to double
v2 <- c(1L,1,1)
print(v2)
is.numeric(v2)
is.integer(v2)
is.double(v2)

# numbers are converted to characters
v3 <- c("a", "b", 10)
print(v3)
is.character(v3)
```

Other functions to create a vector
``` r
# Sequence function
seq(1,10)
1:10
seq(1,59,5)

# Replicate function
rep(5,10)
rep("a",5)
rep(c(1,2),2)
```

Vector elements can be accessed via their index which starts at 1 (not 0). Specifying a negative index will remove element from output vector e.g. v[-2] will output a vectpr without the element at index 2.

``` r
v = c(1,2,3,4,5,6,7,8,9,10)
v[1]
v[-2]
v[2:6]
v[c(2,4,6,8)] # Returns vector with elements in index 2,4,6,8
v[c(-2,-4,-6,-8)] # Returns vector without elements in index 2,4,6,8
v[seq(-1,-5,-2)]
```

Empty vectors with value NA

``` R
# Empty vector
empty = c(NA, NA)
typeof(empty)
empty[1] <- 10
print(empty)
typeof(empty)
```

#### Vector Operations

``` r
v1 <- seq(1,5)
v2 <- rep(10,5)
print(v1)
print(v2)

v1 + v2
v1 - v2
v1 / v2
v1 * v2
```

Operations between unequal vectors will result in the smaller vector being recycled. If larger vecctor length is not an exact multiple of the smaller vector, then R will recycle part of the smaller vector and print a warning.


### Functions

Use inline help "?<function name>" to learn more about builtin or installed functions.

### Packages

Packages are a collection of well defined R functions. Packages are stored in Libraries.

``` R
# Install package
install.packages("package-name")
# Activate Package
library(package-name)
# Test
?function-witin-package()
```

Diamonds dataset sample

``` R
# Install and activate
install.packages("ggplot2")
library(ggplot2)
# Test
?qplot()
?ggplot()
?diamonds

# Sample
qplot(data=diamonds, carat, price, 
      colour=clarity, facets = .~clarity)
```

### Exercise - Financial Analysis

Given the Revenue and Expenses of an org, analyse the following;

1. Profit by month
2. Profit after tax (30%) by month
3. Profit margin in % by month
4. Above average months (when profit is above mean)
5. Below average months
6. Top best and worst month

``` R
#Data
revenue <- c(14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50)
expenses <- c(12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96)

# Use functions
?round()
?mean()
?max()
?min()
?match()

# Solution
profit.gross <- revenue - expenses
# Tax Rate is 30%
profit.net <- profit.gross * 0.7
profit.average <- profit.net / revenue
profit.average <- profit.average * 100
profit.mean <- mean(profit.average)
profit.max <- max(profit.average)
profit.min <- min(profit.average)

profit.good <- profit.average >= profit.mean
profit.bad <- profit.average < profit.mean

print(profit.average)
print(profit.mean)
print(paste(profit.min, profit.max))
print(profit.good)
print(profit.bad)

profit.max_month <- match(profit.max, profit.average)
profit.min_month <- match(profit.min, profit.average)
print(profit.max_month)
print(profit.min_month)
```

### Matrices

A matrix has rows and columns. Index starts from 1.
All elements are of same type. 
Matrices can have named rows and columns.

``` R
m[1]    # Row 1, Column 1
m[5]    # Row 1, Column 5
m[3,4]  # Row 3, Column 4 
m[1,]   # Rowc1
m[,3]   # Column 3


data <- 1:25

m <- matrix(data, nrow=5, ncol=5)
print(m)

n <- matrix(data, nrow=5, ncol=5, byrow = TRUE)
print(n)

o <- rbind(seq(1,5), seq(6, 10))
print(o)

p <- cbind(seq(1,5), seq(6, 10))
print(p)

# Named rows, column
rownames(n) <- c("1","2","3","4","5")
colnames(n) <- c("a","b","c","d","e")

print(n)
print(n["3", "c"]) # element at the center

# Assign value to element
n["3","c"] <- 0

# Clear names
rownames(n) <- NULL
colnames(n) <- NULL
print(n)
```

