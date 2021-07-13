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


