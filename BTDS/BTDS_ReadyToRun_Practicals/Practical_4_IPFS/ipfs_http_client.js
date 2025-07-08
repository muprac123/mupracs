import { create } from 'ipfs-http-client';
const ipfs = create({ url: 'http://localhost:5001/api/v0' });
async function addAndRetrieve() {
  const { cid } = await ipfs.add('Hello IPFS!');
  console.log('CID:', cid.toString());
  const chunks = [];
  for await (const chunk of ipfs.cat(cid)) chunks.push(chunk);
  const content = Buffer.concat(chunks).toString();
  console.log('Content:', content);
}
addAndRetrieve();
