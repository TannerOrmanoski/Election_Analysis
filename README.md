## Election_Analysis

## Overview of the Election Audit

The purpose of this election audit analysis was to help Tom, a Colorado Board of Elections employee, audit the tabulated results of an Election. This election took place in a congressional precinct in Colorado. In this analysis, I was tasked with getting the total number of votes cast, the number of votes each candidate received, and the percentage of the total vote that each candidate received. I also had to determine the winner of the election and find the county with the largest voter turnout. This process was to be completed using Python, to automate the process, so it can be used in future elections. 

## Election-Audit Results 

• In this election there were a total of 369,711 votes cast. 

• 10.5% of the votes came from Jefferson County with 38,855 votes. 82.8% of the votes were from Denver County with 306,055 votes. 6.7% of the votes came from Arapahoe County with 24,801 votes. This information was gathered by creating a list of the unique county names, and then tallying each instance of a county’s name thereafter to arrive at the sum of votes cast in each county. Afterwards simple math was used that converted the number of votes for each county into a percentage.

![](https://github.com/TannerOrmanoski/Election_Analysis/blob/main/county_names_code.png)

• The county with the largest number of votes, was Denver County. The code used to determine this, looped through the list of counties comparing them to each other in a linear fashion, and the county with largest vote number was placed in the largest turnout variable.

![](https://github.com/TannerOrmanoski/Election_Analysis/blob/main/Largest_county_turnout_image.png)

• The three candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Charles accumulated 23% of the vote, with 85,213 votes. Raymon only had 3.1% of the vote, with 11,606 votes. Diana wiped the board with a whopping 272,892 votes, or 73.8% of the total votes. This information was gathered in much the same way as the county information was gathered, with the county variables switched for ones pertaining to the candidates. Since the data included candidate names and county names on each line of data, or ballot, the only other thing that had to be changed was the reference index, from the row containing the county names to the row containing the candidate’s names.

![](https://github.com/TannerOrmanoski/Election_Analysis/blob/main/candidate_name.png)

• Diana was the overwhelming winner with 272,892 votes which equaled 73.8% of the total votes. This was determined in the same manner as the largest voter turnout was, like before, the only thing that really needed to be changed was the variables and the references. (Photo)

## Election-Audit Summary 

This script is simple enough to be of use in any election! It can be used to determine the winner of a bigger election and is versatile enough to handle a larger number of candidates. It can also be used to analyze votes on bills and legislation, rather than candidates. Another great idea would be to use this script to analyze voter demographics. With a few alterations, any of these tasks can be accomplished. The script is already able to handle more candidates because its code can add any other unique values (other candidate names) and store them in its preexisting list. Furthermore, simply swapping out the candidate names and other candidate variables, for bill names or names of other legislation will allow us to bring the second idea into fruition. Finally, since this code can access other csv data based on row index, by including demographic data on the ballot, the user could easily analyze and better understand the voting population.
