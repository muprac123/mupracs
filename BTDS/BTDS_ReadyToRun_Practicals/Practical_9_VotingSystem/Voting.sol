// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Voting {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    mapping(address => bool) public voters;
    mapping(uint => Candidate) public candidates;
    uint public candidatesCount;
    address public admin;
    event VoteCast(address indexed voter, uint indexed candidateId);
    modifier onlyAdmin() { require(msg.sender == admin, "Only admin"); _; }
    constructor() { admin = msg.sender; }
    function addCandidate(string memory _name) public onlyAdmin {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }
    function vote(uint _candidateId) public {
        require(!voters[msg.sender], "Already voted");
        voters[msg.sender] = true;
        candidates[_candidateId].voteCount++;
        emit VoteCast(msg.sender, _candidateId);
    }
    function getVoteCount(uint _candidateId) public view returns (uint) {
        return candidates[_candidateId].voteCount;
    }
}
