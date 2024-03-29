# R language

The R-language has a steep learning curve, so focus and pay attention. Its is a specialised language created for Data Analysis and Statistical Predictive Modeling. It is not a general-purpose programming language. 

Google recommended for Data Analysis.

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
rownames(n) <- c("1","2","3","4","5") # Numbers are also strings 
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

Matrix operations are similar to vector operations, the matrices involved must be of the same dimensions.

### Subsetting

#### Vectors

``` R
v = c("a","b","c","d","e")

# Subset of v with values at index 1,5
v[c(1,5)]
# Sibset of v with value at index 4
v[4]
```

#### Matrices

``` R
data <- 1:25
m <- matrix(data, nrow=5, ncol=5, byrow = T)
print(m)

# Subset of m, Row 2,3, Columns 3 to 5
m2 <- m[2:3, 3:5]
print(m2)
m3 = m[c(2,3), c(3:5)]
print(m3)

```

When the subset is a single row or value the output is converted to a vector. For output to be a matrix use the `drop=FALSE` parameter. The extra dimension is not dropped.

``` R
m1 <- m[1,1]
print(m1)
is.vector(m1)

m1 <- m[1,1, drop=F]
print(m1)
is.matrix(m1)
```

### Exercise - IPL statistics

Create matrices for top 10 IPL batsmen, row names are the player names, column names are the years 2015 - 2019.

1. Number of matches
2. Number of 6's
3. Number of 4's
4. Centuries
5. Half-centuries
6. Times bowled out
7. Times caught
8. Deliveries faced
9. Deliveries scored
10. Auction Price

Create player performance statostics.
Visualise with Matplot function.

### Matplot

Matplot will plot columns, if you want to plot rows then transpose the matrix.

``` R
data <- seq(1,25)
n <- matrix(data, nrow=5, ncol=5)
print(n)
# Transpose function t
n <- t(n)
print(n)
```

ToDo: Matplot sample code

### Functions

``` R
create.matrix <- function(nrows, ncolumns=5) {
  m <- matrix(1:25, nrow = nrows, ncol = ncolumns, byrow = T)
  return(m)
}

m.new <- create.matrix(5)
print(m.new)
```

### Data Frames

Data Frames can have named columns, but rows are always numbered with starting index is 1.
Data frames unlike matrices can contain columns of any type.

``` R
df1 = data.frame(Stat1=c(1:5), Start2=c(21:25), Words=c("One", "Two", "Three", "Four", "Five"))


# Extract column data as vector
col.3 <- df1$<column_name>

# or 
col.3 <- df1[, "<column_name>"]

# Extract single value
col.3 <- df1$<column_name>[2]

```

#### Add Column

``` R
df$<new column name> <- c(1:100)
```

The vector being added as a column must be the same length as the column or a multiple of it as the vector will be recycled (repeated).

#### Remove Column

``` R
df$<column name> <- NULL
```

#### Subsetting

The row numbers are retained in the subset data frame.
Single row subset is not converted into a vector (unlike a matrix). However, single column is. Use `drop=F` to maintain structure.

``` R
df[1:5,] # Rows 1-5, all columns
df[c(1,10),] # Rows 1 and 10, all columns

# Single row subset
is.data.frame(df[1,]) # check is single row subset is also a data frame

# Single column subset
is.data.frame(df[,1])
is.data.frame(df[,1,drop=F])
```

#### Filtering

``` R
filter1 <- df$Birth.rate < 25
head(df[filter1,])

filter2 <- df$Birth.rate < 25 & df$Income.Group == "Low income"
head(df[filter2,])
```

#### Merge Data frames

``` R
# New data frame from match of df1.ColName1 with df2.ColName2
df3 = merge(df1, df2, by.x="ColName1", by.y="ColName2")
str(df3)
head(df3)
summary(df3)
```

#### Factor

Certain columns, e.g. a year column is usually used to categorise data. Its not used as a numeric value. Converting this column from an int into a number will allow for grouping by that column i.e. column is now a factor instead of an int.

e.g. Movie Rating db, "Year" column is originally an int, convert to a factor

``` R
# Movie Ratings db
df <- read.csv(file.choose())
str(df)
summary(df)
head(df)
factor(df$Year.of.release)

# Convert column to factors
df$Year.of.release <- factor(df$Year.of.release)
df$Genre <- factor(df$Genre)

str(df)
```

### Importing data

``` R
?read.csv()

# Prompt
df <- read.csv(file.choose())

# Display Working Directory
getwd()

# Set Working Directory
setwd("C:\\Path to Dir") # On Windows escape "\"

df <- read.csv("filename.csv")
print(df)
```

### Data Navigation

``` R
# Number of rows
nrow(df)

# Number of columns
ncol(df)

# Top 5 rows
head(df, n=5)

# Bottom 5 rows
tail(df, n=5)

# Object Structure
str(df)

# Object Summary
summary(df)

# Factors in vector
levels(df$<column_name>)
```

### Visualisation

[Charles Minard](https://www.nationalgeographic.com/culture/article/charles-minard-cartography-infographics-history)

Components of a Graph/Plot are;
1. Data
2. Aesthetics
3. Geometries
4. Statistics
5. Facets
6. Coordinates
7. Themes


#### qplot

``` R
# GPlot
install.packages("ggplot2") # Download
library(ggplot2) # Install
?qplot()


# Load data
qplot(data=df, x=Internet.users)
qplot(data=df, x=Income.Group, y=Birth.rate)
qplot(data=df, x=Income.Group, y=Birth.rate, size=I(2))
qplot(data=df, x=Income.Group, y=Birth.rate, size=I(2),
      colour=I("blue"))
qplot(data=df, x=Income.Group, y=Birth.rate, size=I(2),
      colour=I("blue"), geom="boxplot")


# Scatter Plot of relation
qplot(data=df, x=Internet.users, y=Birth.rate)
qplot(data=df, x=Internet.users, y=Birth.rate, 
      size=I(3), colour=I("red"))
qplot(data=df, x=Internet.users, y=Birth.rate, 
      size=I(3), colour=Income.Group)


# Visualise Merged data frame
qplot(data=df_all, x=Internet.users, y=Birth.rate)
qplot(data=df_all, x=Internet.users, y=Birth.rate, colour=Region)
qplot(data=df_all, x=Internet.users, y=Birth.rate, colour=Region, 
      size=I(3), shape=I(19), aplha=I(0.5),
      main="Birth Rate v/s Internet Users")
```

#### Ggplot

``` R
# GPlot
install.packages("ggplot2") # Download
library(ggplot2) # Install


```

