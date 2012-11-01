require(deSolve)

zombie.model <- function (t, x, params) {
  S <- x[1]
  V <- x[2]
  I <- x[3]
  R <- x[4]
  with (
    as.list(params),
{
	dS <- -beta*S*I - sigma*S
	dV <- sigma*S
	dI <- beta*S*I - gamma*I
	dR <- gamma*I
  res <- c(dS,dV,dI,dR)
  list(res)
}
  )
}

times <- seq(0,100,by=0.05)
params <- c(
 beta <- 0.50,
 gamma <- 1/10,
 sigma <- 0.01
)

xstart <- c(S = 0.99999, V=0, I = 0.00001, R= 0)

out <- as.data.frame(lsoda(xstart,times,zombie.model,params))

plot(I~time, data=out, ylim=c(0,1.1), type="l", col="red3", lwd=2, ylab="People", xlab="Time (Days)")
lines(S~time, data=out, type="l", col="darkgreen", lwd=2)
lines(V~time, data=out, type="l", col="orange",lwd=2)
lines(R~time, data=out, type="l", col="blue", lwd=2)
legend("topleft", c("Survivors","Vaccinated","Zombies","Dead"), col=c("darkgreen","orange","red3","blue"), lwd=c(2,2,2,2), bty='y', ncol=4)
