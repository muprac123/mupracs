// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract DataIntegrity {
    event DataHashRegistered(address indexed sender, bytes32 dataHash, uint256 timestamp);
    mapping(bytes32 => uint256) public dataHashes;
    function registerDataHash(bytes32 _dataHash) public {
        require(dataHashes[_dataHash] == 0, "Already registered");
        dataHashes[_dataHash] = block.timestamp;
        emit DataHashRegistered(msg.sender, _dataHash, block.timestamp);
    }
    function verifyDataHash(bytes32 _dataHash) public view returns (bool) {
        return dataHashes[_dataHash] != 0;
    }
    function getTimestamp(bytes32 _dataHash) public view returns (uint256) {
        require(dataHashes[_dataHash] != 0, "Not found");
        return dataHashes[_dataHash];
    }
}
