library(GillespieSSA)
x0 <- c(S=499, I=1, R=0)
a <- c("0.50*{S}*{I}/({S}+{I}+{R})","0.1*{I}")
nu <- matrix(c(-1,0,
               +1,-1,
               0, +1),nrow=3,byrow=T)

out <- lapply(X=1:10,FUN=function(x) ssa(x0, a, nu, tf=100)$data)

plot(out[[1]][,1],out[[1]][,2], ylim=c(0,500), col="red3", type="l")
nruns <- 10
for (i in 2:nruns){lines(out[[i]][,1],out[[i]][,2])}