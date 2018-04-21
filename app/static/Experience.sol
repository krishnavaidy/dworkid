/*
DWorkID contract
A contract that is created for a person.
A person can add experience of working for a particular company, and this can be verified by a company
*/


pragma solidity ^0.4.19;


contract Experience {
    
    struct experience_struct {
    address employer;
    uint8 status; // 2 if pending, 0 if rejected, 1 if approved
    }
    address employee;
    mapping (string => experience_struct) exp;
    
    constructor() public {
        employee = msg.sender;
    }
    
    function addExperience(string _message, address _employer) public {
        require(msg.sender == employee);
        experience_struct memory _exp = experience_struct({employer: _employer, status: 2});
        exp[_message] = _exp;
    }
    
    function approveExperience(string _message) public {
        require(msg.sender == exp[_message].employer); // makes sure that the user that approves the experience is the same as the user specified in the experience
        exp[_message].status = 1;
    }
    
    function rejectExperience(string _message) public {
        require(msg.sender == exp[_message].employer);// makes sure that the user that rejects the experience is the same as the user specified in the experience
        exp[_message].status = 0;
    }
    
    function getStatus(string _message) public view returns (uint8) {
        return exp[_message].status;
    }
}
