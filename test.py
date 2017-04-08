import byteball

bb = byteball.Api()

#print bb.getWallets()
#print bb.getAddresses()
#print bb.getAddress("MZ4GUQC7WUKZKKLGAS3H3FSDKLHI7HFO")
#print bb.getBalls()
#print bb.getUnitWitnesses()
#print bb.getMessages()[0]
#print bb.getMessagesByApp("payment")
#print bb.getSpentProofs()
#print bb.getInputPayments()
#print bb.getOutputPayments()
#print bb.getPeers()
print bb.getSharedAddresses()

bb.close()
