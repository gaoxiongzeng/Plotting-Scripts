# File address and name.
myfile <- "D:\\temp\\R\\figures\\linechart.pdf"

# Load the data.
dataa <- c(162, 186, 256, 438)
datab <- c(200, 217, 251, 310)
datac <- c(161, 185, 233, 298)
datad <- c(89, 98, 107, 116)
myxann <- c("Case A", "Case B", "Case C", "Case D")
myylab <- "Label Y"
mylegend <- c("Legend A", "Legend B", "Legend C", "Legend D")

# Basic setup.
myylim <- c(0,500)
colormap <- c(rgb(0.93,0.49,0.19,1), rgb(0.36,0.61,0.84,1), 
	rgb(1,0.75,0,1), rgb(0.3,0.3,0.3,1))
pdf(file=myfile, width=11, height=7)
par(mar=c(2,3,0.5,1), cex=2.4, cex.lab=1.2, mgp=c(2,0.5,0))

# Plot the chart.
plot(dataa, type="o", pch=15, cex=1.5, 
	col=colormap[1], lwd=8,
	ylab=myylab, ylim=myylim, xaxt="n")
lines(datab, type="o", pch=16, cex=1.5, 
	col=colormap[2], lwd=8)
lines(datac, type="o", pch=17, cex=1.5, 
	col=colormap[3], lwd=8)
lines(datad, type="o", pch=18, cex=1.5, 
	col=colormap[4], lwd=8)

# Add the customized xaxis.
axis(1, at=1:4, labels=FALSE)
text(1:4, y=-70, labels=myxann, srt=15, xpd=TRUE)

# Add the legend.
legend("topleft", inset=0.02, legend=mylegend, 
	lty=1, lwd=8, pch=c(15,16,17,18), pt.cex=1.5, col=colormap)

# Save the file.
dev.off()