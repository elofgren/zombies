#Specify the length of time the model will be run for
t <- 100

#Create array to take model output, and name the columns appropriately
output <- array(dim=c(t+1,5))
colnames(output) <- c("S", "I", "R", "N", "Time")

#Specify initial populations in each compartment
output[1,"S"] <- 999
output[1,"I"] <- 1
output[1,"R"] <- 0
output[1,"N"] <- 1000
output[1,"Time"] <- 0

#Assign values to the two transmission parameters beta and gamma
beta <- 0.50
gamma <- 1/10

# Run the model for every time step except time 1 (which was set to fixed above)
for (i in 2:(t+1)){
  output[i,"S"] <- max(output[i-1,"S"] - beta*output[i-1,"S"]*output[i-1,"I"]/output[i-1,"N"],0)
  output[i,"I"] <- max(output[i-1,"I"] + beta*output[i-1,"S"]*output[i-1,"I"]/output[i-1,"N"] - gamma*output[i-1,"I"],0)
  output[i,"R"] <- max(output[i-1,"R"] + gamma*output[i-1,"I"],0)
  output[i,"N"] <- max(output[i,"S"]+output[i,"I"]+output[i,"R"],1)
  output[i,"Time"] <- output[i-1,"Time"]+1
}

#Plot I against Time, then add lines for other categories and a legend
plot(I~Time, data=output, type="l", col="Red", ylim=c(0,1100), xlab="Days", ylab="People")
lines(S~Time, data=output, type="l", col="Darkgreen")
lines(R~Time, data=output, type="l", col="Blue")
lines(N~Time, data=output, type="l", col="Black", lty=2)
legend("topright", c("S","I","R"), lwd=2, col=c("darkgreen","red","blue"), lty=c(1,1,1), bty='y',ncol=3)