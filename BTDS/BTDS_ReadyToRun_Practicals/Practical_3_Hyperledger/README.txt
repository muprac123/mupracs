This practical uses Hyperledger Fabric Test Network.

Commands:
cd fabric-samples/test-network
./network.sh up createChannel -c mychannel -ca
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
docker exec -it cli bash
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'
./network.sh down
