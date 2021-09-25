    pragma solidity ^0.6.2;

    contract tokenHandlers {
        address owner;
        constructor () public  {
            owner = msg.sender;
        }
        modifier onlyOwner() {
            require(owner == msg.sender,'Not authorized');
            _;
        }
        uint base_price = 0.069 ether;
        uint coolDownTime = 2 days;
        mapping (address => bool) public whiteListedAddress;
        function createTokens(address _user) external onlyOwner returns (bool) {
            require(whiteListedAddress[_user] == false,'User exists');
            whiteListedAddress[_user] = true;
            return true;
        }

        function setPrice(uint _amount) private onlyOwner returns(uint,bool) {
            base_price = _amount;
            return (_amount, true);
        }
    }