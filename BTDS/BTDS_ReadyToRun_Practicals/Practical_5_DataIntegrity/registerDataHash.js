const fs = require('fs');
const crypto = require('crypto');
const Web3 = require('web3');
const contractABI = require('./build/contracts/DataIntegrity.json').abi;
const contractAddress = 'YOUR_CONTRACT_ADDRESS';
async function main() {
  const data = fs.readFileSync('dataset.csv');
  const hash = crypto.createHash('sha256').update(data).digest('hex');
  const web3 = new Web3('http://127.0.0.1:7545');
  const accounts = await web3.eth.getAccounts();
  const contract = new web3.eth.Contract(contractABI, contractAddress);
  await contract.methods.registerDataHash('0x' + hash).send({ from: accounts[0], gas: 300000 });
}
main();
