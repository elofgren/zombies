require(deSolve)

zombie.model <- function (t, x, params) {
  S <- x[1]
  I <- x[2]
  R <- x[3]
  with (
    as.list(params),
{
	dS <- -beta*S*I/(S+I+R)
	dI <- beta*S*I/(S+I+R) - gamma*I
	dR <- gamma*I
  res <- c(dS,dI,dR)
  list(res)
}
  )
}

times <- seq(0,100,by=0.05)
params <- c(
 beta <- 0.50,
 gamma <- 1/10
)

xstart <- c(S = 999, I = 1, R= 0)

out <- as.data.frame(lsoda(xstart,times,zombie.model,params))

plot(I~time, data=out, ylim=c(0,1100), type="l", col="red3", lwd=2, ylab="People", xlab="Time (Days)")
lines(S~time, data=out, type="l", col="darkgreen", lwd=2)
lines(R~time, data=out, type="l", col="blue", lwd=2)
legend("topleft", c("Survivors","Zombies","Dead"), col=c("darkgreen","red3","blue"), lwd=c(2,2,2), bty='y', ncol=3)
