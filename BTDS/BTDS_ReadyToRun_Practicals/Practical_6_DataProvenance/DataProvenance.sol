// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract DataProvenance {
    struct ProvenanceEvent {
        address actor;
        uint256 timestamp;
        string operation;
        string description;
    }
    mapping(bytes32 => ProvenanceEvent[]) private provenanceRecords;
    event ProvenanceRecorded(bytes32 indexed dataId, address indexed actor, string operation, uint256 timestamp);
    function recordEvent(bytes32 dataId, string memory operation, string memory description) public {
        provenanceRecords[dataId].push(ProvenanceEvent(msg.sender, block.timestamp, operation, description));
        emit ProvenanceRecorded(dataId, msg.sender, operation, block.timestamp);
    }
    function getEventCount(bytes32 dataId) public view returns (uint256) {
        return provenanceRecords[dataId].length;
    }
    function getProvenanceEvent(bytes32 dataId, uint256 index) public view returns (address, uint256, string memory, string memory) {
        ProvenanceEvent storage evt = provenanceRecords[dataId][index];
        return (evt.actor, evt.timestamp, evt.operation, evt.description);
    }
}
