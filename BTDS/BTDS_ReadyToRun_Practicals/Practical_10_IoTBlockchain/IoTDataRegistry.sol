// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract IoTDataRegistry {
    struct DataRecord {
        bytes32 dataHash;
        uint256 timestamp;
        address device;
    }
    DataRecord[] public records;
    event DataRegistered(bytes32 indexed dataHash, uint256 timestamp, address indexed device);
    function registerData(bytes32 _dataHash) public {
        records.push(DataRecord(_dataHash, block.timestamp, msg.sender));
        emit DataRegistered(_dataHash, block.timestamp, msg.sender);
    }
    function getRecordsCount() public view returns (uint256) {
        return records.length;
    }
    function getDataRecord(uint256 index) public view returns (bytes32, uint256, address) {
        DataRecord storage record = records[index];
        return (record.dataHash, record.timestamp, record.device);
    }
}
