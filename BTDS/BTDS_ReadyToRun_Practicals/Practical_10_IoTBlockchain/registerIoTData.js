const Web3 = require('web3');
const crypto = require('crypto');
const fs = require('fs');
const contractABI = require('./build/contracts/IoTDataRegistry.json').abi;
const contractAddress = 'YOUR_DEPLOYED_CONTRACT_ADDRESS';
async function registerIoTData(filePath) {
  const data = fs.readFileSync(filePath);
  const hash = crypto.createHash('sha256').update(data).digest('hex');
  const web3 = new Web3('http://127.0.0.1:7545');
  const accounts = await web3.eth.getAccounts();
  const contract = new web3.eth.Contract(contractABI, contractAddress);
  const receipt = await contract.methods.registerData('0x' + hash).send({ from: accounts[0], gas: 300000 });
  console.log('Data registered in transaction:', receipt.transactionHash);
}
registerIoTData('sensor_data.json').catch(console.error);
