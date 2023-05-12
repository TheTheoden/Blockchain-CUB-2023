pragma solidity 0.8.7;

contract VendingMachine {
    address public owner;
    mapping(address => uint) public cupcakeBalances;
    mapping(address => uint) public etherBalances;
    mapping(address => mapping(address => uint)) public tokenBalances;

    constructor() {
        owner = msg.sender;
        cupcakeBalances[address(this)] = 100;
    }

    function refill(uint amount) public {
        require(msg.sender == owner, "Only the owner can refill.");
        cupcakeBalances[address(this)] += amount;
    }

    function purchase(uint amount) public payable {
        require(msg.value >= amount * 1 ether, "You must pay at least 1 ETH per cupcake");
        require(cupcakeBalances[address(this)] >= amount, "Not enough cupcakes in stock to complete this purchase");
        cupcakeBalances[address(this)] -= amount;
        cupcakeBalances[msg.sender] += amount;
    }

    function exchangeEtherForToken(address token, uint amount) public {
        require(etherBalances[msg.sender] >= amount, "Not enough Ether balance to complete this exchange");
        require(token != address(0), "Invalid token address");

        etherBalances[msg.sender] -= amount;
        tokenBalances[msg.sender][token] += amount;
    }

    function exchangeTokenForEther(address token, uint amount) public {
        require(tokenBalances[msg.sender][token] >= amount, "Not enough token balance to complete this exchange");
        require(token != address(0), "Invalid token address");

        tokenBalances[msg.sender][token] -= amount;
        etherBalances[msg.sender] += amount;
    }

}