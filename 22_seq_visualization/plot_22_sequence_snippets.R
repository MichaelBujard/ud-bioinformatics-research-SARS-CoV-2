# DESCRIPTION ######################
# file name: plot_22_sequence_snippets.R
# Purpose: Data visualization.
# Note: This could be used for an arbitrarily long file. However, the 
# plots would become very big.
# This description was written and the file pushed to GitHub on April 23, 2021
##

# IMPORT PACKAGES #############################
# import ggplot2 data visualization library for plotting
# import data.table for enhanced data storage capabilities

library(data.table)
library(ggplot2)

# GET AND STORE DATA #############################

# Get the main file and read it

snippets <- read.csv(file = '22_snippet_occurrences.csv')

# look at a "sneak peak" of the file, 
# to see what it looks like

head(snippets)

# make a table where column names are numbered according to number of snippets,
# and the row entry for each column is the number of S protein sequence pairs
# that have the number of snippets corresponding to a column.
# That is, if 1 is the name of the column and 39 is the number in the first 
# and only row beneath it, then the number of sequence pairs with 1 snippet
# occurrence is 39. That is, in 39 out of 154 pairs of aligned 
# amino acid (AA) sequences, 
# there is just 1 instance of a mismatch, or snippet occurrence in the 
# compared AA sequences.

snippet_table <- table(snippets$AA_MISMATCHES)

print(snippet_table)

numberIDs <- length(snippets$SEQUENCE_PAIRS)
print(numberIDs)
        
# get data and organize it as a data frame
df <- data.frame(group = c(rep(snippets$SEQUENCE_PAIRS)),
                 values = snippets$AA_MISMATCHES)

# another way to get data, with x-values being the 1st, 2nd, ..., nth id in file
# as the x-values.
# get data and organize it as a data frame
dfTwo <- data.frame(group = c(seq(1, numberIDs, 1)),
                 values = snippets$AA_MISMATCHES)

# PLOT ################################################
# Plotting the snippet table. Basic plot. Numbers along the x-axis
# correspond to the columns, and y-values to row entries for each column in
# the snippet_table above.
plot(snippet_table,
     main="Frequency vs. Pairs",
     xlab="Snippet Occurrence Frequency",
     ylab="Spike Protein Sequence Pairs")

# a slightly more aesthetic visualization with title and x-, y-labels.
barplot(snippet_table,
        col='dark red',
        main="Frequency vs. Pairs",
        xlab="Snippet Occurrence Frequency", 
        ylab="Spike Protein Sequence Pairs",
        xlim=c(0,30),
        ylim=c(0,40)
)

print(length(snippets$SEQUENCE_PAIRS))
print(length(numberIDs))

# using ggplots2 library, plot with x-labels being the accession ID pairs
ggplot(df) + 
        geom_bar(aes(group, values, fill = group), stat = "identity", width = .8) +
        ylab("Snippet Frequency") +
        ylab("Snippet Frequency") +
        ggtitle("Snippet Occurrence Per Sequence Comparison") +
        theme(legend.position = "none", 
              axis.text.x = element_text(angle = 45,
                                         hjust = 1,
                                         size = 5,
                                         margin = margin(r=0)),
              plot.title = element_text(hjust = 0.5))

# another plot, barplot, trying numeric representation of accession data
ggplot(df) + 
        geom_bar(aes(group, values, fill = group), stat = "identity", width = .8) +
        ylab("Snippet Frequency") +
        scale_x_discrete(name="Sequence Pairs",
                         breaks = snippets$SEQUENCE_PAIRS,
                         labels= 1 : numberIDs) +
        ggtitle("Snippet Occurrence Per Sequence Comparison") +
        theme(legend.position = "none", 
              axis.text.x = element_text(angle = 45,
                                         hjust = 1,
                                         size = 5,
                                         margin = margin(r=0)),
              plot.title = element_text(hjust = 0.5))

rlang::last_error()

# try using graphics devices (png) to set the exact width and height of the image

# (5) another plot
ggplot(dfTwo) +
        geom_bar(aes(group, values, fill = group), stat = "identity", width = .8) +
        ylab("Snippet Frequency") +
        xlab("Sequence Pairs") +
        scale_x_continuous(breaks = pretty(1 : numberIDs, n=153)) +
        ggtitle("Snippet Occurrence Per Sequence Comparison") +
        theme(legend.position = "none",
              axis.text.x = element_text(angle = 45,
                                         hjust = 1,
                                         size = 6,
                                         margin = margin(r=0)),
              plot.title = element_text(hjust = 0.5))


rlang::last_error()

# SUPPLEMENTARY DATA VISUALIZATION TOOLS ######################

# Build a table that maps the accession ID pairs to the plots

barplotFrame <- data.frame('accession_id_pair'=snippets$SEQUENCE_PAIRS,
                           'x_axis_tick'=1:numberIDs)

print(barplotFrame)
# LAST THINGS #################################################

# clean environment
rm(list = ls()) 

# Detach packages
detach("Package:ggplot2", unload = TRUE)
detach("package:data.table", unload = TRUE)

# Remove plots
dev.off()

# Clean console
cat("\014")
# END #########################

