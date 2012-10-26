#Specify the length of time the model will be run for
t = 10000

#Create array to take model output, and name the columns appropriately
output <- array(dim=c(t+1,6))
colnames(output) <- c("S","I","R","W","N","Time")

#Specify initial populations in each compartment
output[1,"S"] <- 9999
output[1,"I"] <- 1
output[1,"R"] <- 0
output[1,"W"] <- 0
output[1,"N"] <- 10000
output[1,"Time"] <- 0

#Assign values to the two transmission parameters beta and gamma
beta <- 0.714
gamma <- 1/21
nu <- 0.80
omega <- 1/(5*365.25)
kappa <- 1
mu <- 1/(70*365.25)

# Run the model for every time step except time 1 (which was set to fixed above)
for (i in 2:(t+1)){
  output[i,"S"] <- max(output[i-1,"S"] - (beta*output[i-1,"S"]*output[i-1,"I"]/output[i-1,"N"]) + omega*output[i-1,"W"]
    +(mu*(1-nu))*output[i-1,"N"]-mu*output[i-1,"S"],0)
  output[i,"I"] <- max(output[i-1,"I"] + (beta*output[i-1,"S"]*output[i-1,"I"]/output[i-1,"N"]) - gamma*output[i-1,"I"]
    -mu*output[i-1,"I"],0)
  output[i,"R"] <- max(output[i-1,"R"] + gamma*output[i-1,"I"]+(beta*kappa*output[i-1,"W"]*output[i-1,"I"]/output[i-1,"N"])
    -omega*output[i-1,"R"]+mu*nu*output[i-1,"N"]-mu*output[i-1,"R"],0)
  output[i,"W"] <- max(output[i-1,"W"] +omega*output[i-1,"R"] - (beta*kappa*output[i-1,"W"]*output[i-1,"I"]/output[i-1,"N"])
    -omega*output[i-1,"W"]-mu*output[i-1,"W"],0)  
  output[i,"N"] <- max(output[i,"S"]+output[i,"I"]+output[i,"R"]+output[i,"W"],0)
  output[i,"Time"] <- output[i-1,"Time"]+1
}

#Plot I against Time, then add lines for other categories and a legend
plot(I~Time, data=output, type="l", col="Red", ylim=c(0,11000), xlab="Days", ylab="People")
lines(S~Time, data=output, type="l", col="Darkgreen")
lines(R~Time, data=output, type="l", col="Blue")
lines(W~Time, data=output, type="l", col="Orange")
lines(N~Time, data=output, type="l", col="Black", lty=2)
legend("topleft", c("S","I","R","W"), lwd=2, col=c("darkgreen","red","blue","orange"), lty=c(1,1,1,1), bty='y',ncol=4)
