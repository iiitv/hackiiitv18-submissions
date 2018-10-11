pragma solidity ^0.4.17;

contract Store {
    address[] public deployedProjects;
    
    function createProject(uint min, string projectName, string projectDesc, string creatorName, string creatorContact) public{
        address newProject = new Project(min, msg.sender, projectName, projectDesc, creatorName, creatorContact);
        deployedProjects.push(newProject);
    }
    function getDeployedProjects() public view returns (address[]){
        return deployedProjects;
    }
}

contract Project {
    
    struct Request{
        string description;
        string contact;
        uint value;
        address recipient;
        bool complete;
        uint approvalCount;
        mapping(address => bool) approvals;
    }
    
    Request[] public requests;
    address public manager;
    uint public minContribution;
    uint public approversCount;
    mapping (address => bool) public approvers;
    
    string public projectName;
    string public projectDesc;
    string public creatorName;
    string public creatorContact;
    
    modifier onlyManager{
        require(msg.sender == manager);
        _;
    }

    constructor (uint minimum, address creator, string ProjectName, string ProjectDesc, string CreatorName, string CreatorContact) public{
        manager = creator;
        minContribution = minimum;
        projectName = ProjectName;
        projectDesc = ProjectDesc;
        creatorName = CreatorName;
        creatorContact = CreatorContact;
    }
    
    function contribute(bool addMe) public payable {
        
        require(msg.value >= minContribution);
        if(addMe){    
            require(!approvers[msg.sender]);
            
            approvers[msg.sender] = true;
            approversCount++;
        }    
    }
    
    function createRequest(string description, string contact, uint value, address recipient) public onlyManager{
        
        Request memory newRequest = Request({
            description: description,
            contact: contact, 
            value: value,
            recipient: recipient,
            complete: false,
            approvalCount: 0
        });
        
        requests.push(newRequest);
    }
    
    function approveRequest(uint index) public {
    
        require(approvers[msg.sender]);
        require(!requests[index].approvals[msg.sender]);
        
        requests[index].approvals[msg.sender] = true;
        requests[index].approvalCount++;
    }
    
    function finalizeRequest(uint index) public onlyManager{
        
        require(requests[index].approvalCount > (approversCount)/2);
        require(!requests[index].complete);
        
        requests[index].recipient.transfer(requests[index].value);
        requests[index].complete = true;
    }
}
