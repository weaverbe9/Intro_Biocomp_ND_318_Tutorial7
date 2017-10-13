import pandas

        # Lecture 11 notes

# import data
lec11=open("Lecture11.fasta","r")

#how to store stuff
sequenceID=[]
sequenceLength=[]
percentGC=[]
meltingTemp=[]

#beginning of the loop
for line in lec11:
    # remove newline character from file line
    line=line.strip()
    # if a sequence record
    if '>' in Line:
        # add the sequence ID (except the ">" character) to the sequenceID list
        sequenceID.append(line[1:])
    # if a sequence line
    else:
        # get the number of characters in the sequence and convert to a float to avoid integer division
        seqLen=float(len(line))
        # count the number of G's and C's
        nG=line.count("G")
        nC=line.count("C")
        
        # if the sequence is 14 or fewer bases calculate melting temperature
        if seqLen<=14:
            Tm=2*(nG+nC)+2*seqLen
        else:
            Tm=-9999
        
        # append values to the lists
        sequenceLength.append(seqLen)
        percentGC.append((nG+nC)/seqLen*100)
        meltingTemp.append(Tm)

# make a dataframe to combine it all
seqDF = pandas.DataFrame(list(zip(sequenceID,sequenceLength,percentGC,meltingTemp)),columns=['sequenceID','sequenceLength','percentGC','meltingTemp'])

        #Exercise 7

#1

#import packages
import numpy
import pandas
#import from plotnine
from plotnine import *

#histogram of sequence lengths
a=ggplot(aes(x='sequenceLength'), data= seqDF)
a+geom_histogram(binwidth=5, fill='orange',color='black')+theme_classic()

#histogram of GC content
b=ggplot(aes(x='percentGC'), data= seqDF)
b+geom_histogram(binwidth=15,fill='green',color='black')+theme_classic()

#2

#import package
import numpy
#import package
import pandas
#import from plotnine
from plotnine import *

turtles=pandas.read_csv("turtles2.csv",header=0)


# plot of %TAG vs. %lipid for unhealthy and healthy turtles with trendline

f=ggplot(turtles,aes(x="%_Lipid",y="%_TAG"))+geom_point(aes(color="Condition"))
f+scale_color_manual(values=['green','red'])+theme_classic()+stat_smooth(method="lm")

#3

#import package
import pandas
#load file
data=pandas.read_csv("data.txt",sep=",",header=0)

#barplot
n=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
n+geom_bar(aes(x="region",y="observations"),stat="summary",fun_y=numpy.mean)

#scatterplot with jitter
o=ggplot(data,aes(x="region",y="observations"))+theme_classic()
o+geom_jitter()+coord_cartesian()
