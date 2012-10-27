library(GillespieSSA)
x0 <- c(S=499, I=1, R=0)
a <- c("0.50*{S}*{I}/({S}+{I}+{R})","0.1*{I}")
nu <- matrix(c(-1,0,
               +1,-1,
               0, +1),nrow=3,byrow=T)
out <- ssa(x0, a, nu, tf=100)

plot(out$data[,1],out$data[,2],type="l", col="blue", lwd=2)
lines(out$data[,1],out$data[,3], type="l", col="red3", lwd=2)
lines(out$data[,1],out$data[,4], type="l", col="grey75", lwd=2)
legend("topright",c("S","I","R"),col=c("blue","red3","grey75"),lwd=c(2,2,2), bty='n')

  
