# File address and name.
myfile <- "D:\\temp\\R\\figures\\barplot.pdf"

# Load the data.
dataa <- c(1968, 1940, 55, 64, 1269)
datab <- c(8021, 8060, 9945, 9936, 8731)
datac <- c(8027, 8060, 9945, 9936, 8731)
myxann <- c("Case A", "Case B", "Case C", "Case D", "Case E")
myylab <- "Label Y"
mylegend <- c("L1", "L2", "L3")

# Basic setup.
myylim <- c(0,10500)
colormap <- c(rgb(0.33,0.56,0.84,0.9), 
	rgb(0.75,0.31,0.3,1), rgb(0.61,0.73,0.35,0.9))
pdf(file=myfile, width=15, height=7)
par(mar=c(2,4,0.5,0.2), cex=2.4, cex.lab=1.2, mgp=c(3,0.5,0), las=1)

# Plot the chart.
barplot(rbind(dataa, datab, datac), beside=TRUE, 
	ylab=myylab, ylim=myylim, col=colormap,
	legend.text=mylegend, 
	args.legend=list(x="topleft",inset=0.02,horiz=TRUE))

# Overwriting texture.
par(new=TRUE)
barplot(rbind(dataa, datab, datac), beside=TRUE,
	ylim=myylim, col="black", 
	density=c(3,3,3), angle=c(45,180,-45),
	legend.text=mylegend, 
	args.legend=list(x="topleft",inset=0.02,horiz=TRUE))

# Add the customized xaxis.
axis(1, at=seq(2.5,18.5,4), labels=FALSE)
text(seq(2.5,18.5,4), y=-900, labels=myxann, srt=10, xpd=TRUE)

# Draw the figure outline.
box()

# Save the file.
dev.off()