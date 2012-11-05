require(deSolve)

zombie.model <- function (t, x, params) {
  S <- x[1]
  H <- x[2]
  E <- x[3]
  I <- x[4]
  R <- x[5]
  K <- x[6]
  with (
    as.list(params),
{
	dS <- -beta*S*I - lam*S
  dH <- lam*S - beta_safe*H*I
  dE <- beta*S*I - alpha*E + beta_safe*H*I
	dI <- alpha*E - gamma*I - kappa*I*H
	dR <- gamma*I
  dK <- kappa*I*H
  res <- c(dS,dH,dE,dI,dR,dK)
  list(res)
}
  )
}

times <- seq(0,200,by=0.02)
params <- c(
 beta <- 0.50,
 beta_safe <- beta/2,
 alpha <- 1/2,
 kappa <- 0.05,
 lam <- 1/14,
 gamma <- 1/10
)

xstart <- c(S = 0.99999, H = 0,E = 0, I = 0.00001, R = 0, K = 0)

out <- as.data.frame(lsoda(xstart,times,zombie.model,params))

plot(S~time, data=out, ylim=c(0,1.1), type="l", col="darkgreen", lwd=2, ylab="Proportion of Population", xlab="Time (Days)")
lines(H~time, data=out, col="blue", lwd=2)
lines(I~time, data=out, col="red3", lwd=2)
lines(E~time, data=out, col="purple", lwd=2)
legend("topright", c("Wandering","Safe","Zombies","Latent"), col=c("darkgreen","blue","red3","purple"), lwd=c(2,2,2,2), bty='y', ncol=2)

plot(R~time, data=out, ylim=c(0,1.1), type="l", col="blue", lwd=2, lty=3, ylab="Proportion of Population",xlab="Time (Days)")
lines(K~time, data=out, type="l", col="grey50", lwd=2)
legend("topright", c("Dead","Culled"), col=c("blue","grey50"), lwd=c(2,2), lty=c(3,1), bty='y', ncol=1)
