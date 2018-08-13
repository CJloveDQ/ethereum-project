pragma solidity ^0.4.16;
contract owned {
    address public owner;

    function owned() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function transferOwnership(address newOwner) onlyOwner public {
        owner = newOwner;
    }
}

interface tokenRecipient {
    function receiveApproval(address _from, uint256 _value, address _token, bytes _extraData) public;
}

contract TokenERC20 {
    // Public variables of the token
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    // 18 decimals is the strongly suggested default, avoid changing it
    uint256 public totalSupply;

    // This creates an array with all balances
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;

    // This generates a public event on the blockchain that will notify clients
    event Transfer(address indexed from, address indexed to, uint256 value);

    // This notifies clients about the amount burnt
    event Burn(address indexed from, uint256 value);

    /**
     * Constrctor function
     *
     * Initializes contract with initial supply tokens to the creator of the contract
     */
    function TokenERC20(
        uint256 initialSupply,
        string tokenName,
        string tokenSymbol
    ) public {
        totalSupply = initialSupply * 10 ** uint256(decimals);  // Update total supply with the decimal amount
        balanceOf[msg.sender] = totalSupply;                // Give the creator all initial tokens
        name = tokenName;                                   // Set the name for display purposes
        symbol = tokenSymbol;                               // Set the symbol for display purposes
    }


    /**
     * Internal transfer, only can be called by this contract
     */
    function _transfer(address _from, address _to, uint _value) internal {
        // Prevent transfer to 0x0 address. Use burn() instead
        require(_to != 0x0);
        // Check if the sender has enough
        require(balanceOf[_from] >= _value);
        // Check for overflows
        require(balanceOf[_to] + _value > balanceOf[_to]);
        // Save this for an assertion in the future
        uint previousBalances = balanceOf[_from] + balanceOf[_to];
        // Subtract from the sender
        balanceOf[_from] -= _value;
        // Add the same to the recipient
        balanceOf[_to] += _value;
        Transfer(_from, _to, _value);
        // Asserts are used to use static analysis to find bugs in your code. They should never fail
        assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
    }

    /**
     * Transfer tokens
     *
     * Send `_value` tokens to `_to` from your account
     *
     * @param _to The address of the recipient
     * @param _value the amount to send
     */
    function transfer(address _to, uint256 _value) public {
        _transfer(msg.sender, _to, _value);
    }

    /**
     * Transfer tokens from other address
     *
     * Send `_value` tokens to `_to` in behalf of `_from`
     *
     * @param _from The address of the sender
     * @param _to The address of the recipient
     * @param _value the amount to send
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= allowance[_from][msg.sender]);     // Check allowance
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }

    /**
     * Set allowance for other address
     *
     * Allows `_spender` to spend no more than `_value` tokens in your behalf
     *
     * @param _spender The address authorized to spend
     * @param _value the max amount they can spend
     */
    function approve(address _spender, uint256 _value) public
        returns (bool success) {
        allowance[msg.sender][_spender] += _value;
        return true;
    }

    /**
     * Set allowance for other address and notify
     *
     * Allows `_spender` to spend no more than `_value` tokens in your behalf, and then ping the contract about it
     *
     * @param _spender The address authorized to spend
     * @param _value the max amount they can spend
     * @param _extraData some extra information to send to the approved contract
     */
    function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }

    /**
     * Destroy tokens
     *
     * Remove `_value` tokens from the system irreversibly
     *
     * @param _value the amount of money to burn
     */
    function burn(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value);   // Check if the sender has enough
        balanceOf[msg.sender] -= _value;            // Subtract from the sender
        totalSupply -= _value;                      // Updates totalSupply
        Burn(msg.sender, _value);
        return true;
    }

    /**
     * Destroy tokens from other account
     *
     * Remove `_value` tokens from the system irreversibly on behalf of `_from`.
     *
     * @param _from the address of the sender
     * @param _value the amount of money to burn
     */
    function burnFrom(address _from, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value);                // Check if the targeted balance is enough
        require(_value <= allowance[_from][msg.sender]);    // Check allowance
        balanceOf[_from] -= _value;                         // Subtract from the targeted balance
        allowance[_from][msg.sender] -= _value;             // Subtract from the sender's allowance
        totalSupply -= _value;                              // Update totalSupply
        Burn(_from, _value);
        return true;
    }
}

/******************************************/
/*       ADVANCED TOKEN STARTS HERE       */
/******************************************/

contract MyAdvancedToken is owned, TokenERC20 {

    uint256 public sellPrice;
    uint256 public buyPrice;
    uint256 public needLockPeriod=7776000;
    mapping (address => bool) public frozenAccount;
    mapping (address => uint) public lockedAmount;
    mapping (address =>invest[]) public investDetails;
    mapping (address =>address) public investAccounts;
    mapping (address => address) public activeAccounts;
    struct invest
    {
      uint investAmount;
      uint lockTime;
      uint investTime;
    }

    /* public event about locking */
    event LockToken(address target, uint256 amount,uint lockPeriod);
    event TransferlockedAmount(address from, address to, uint256 value);
    event OwnerUnlock(address from,address to,uint256 amount);
    /* This generates a public event on the blockchain that will notify clients */
    event FrozenFunds(address target, bool frozen);
    event Bind(address activeAccount,address investAccount);
    /* Initializes contract with initial supply tokens to the creator of the contract */
    function MyAdvancedToken(
        uint256 initialSupply,
        string tokenName,
        string tokenSymbol
    ) TokenERC20(initialSupply, tokenName, tokenSymbol) public {}

      function changeLockPeriod(uint256 newNeedLoackAmount) public onlyOwner()
      {
        needLockPeriod=newNeedLoackAmount;
      }
    /* Internal transfer, only can be called by this contract */
    function _transfer(address _from, address _to, uint _value) internal {
        require (_to != 0x0);                               // Prevent transfer to 0x0 address. Use burn() instead
        require (balanceOf[_from] >= _value);               // Check if the sender has enough
        require (balanceOf[_to] + _value > balanceOf[_to]); // Check for overflows
        require(!frozenAccount[_from]);                     // Check if sender is frozen
        require(!frozenAccount[_to]);                       // Check if recipient is frozen
        uint previousBalances = balanceOf[_from] + balanceOf[_to];
        balanceOf[_from] -= _value;                         // Subtract from the sender
        balanceOf[_to] += _value;                           // Add the same to the recipient
        assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
        Transfer(_from, _to, _value);
    }


    //pay violator's debt by send coin
    function punish(address violator,address victim,uint amount) public onlyOwner
    {
      _transfer(violator,victim,amount);
    }



    function rename(string newTokenName,string newSymbolName) public onlyOwner
    {
      name = newTokenName;                                     // Set the name for display purposes
      symbol = newSymbolName;
    }


    function mintToken(address target, uint256 mintedAmount) onlyOwner public {
        balanceOf[target] += mintedAmount;
        totalSupply += mintedAmount;
        Transfer(0, this, mintedAmount);
        Transfer(this, target, mintedAmount);
    }


    function freezeAccount(address target, bool freeze) onlyOwner public {
        frozenAccount[target] = freeze;
        FrozenFunds(target, freeze);
    }


    function setPrices(uint256 newSellPrice, uint256 newBuyPrice) onlyOwner public {
        sellPrice = newSellPrice;
        buyPrice = newBuyPrice;
    }


    function buy() payable public {
        uint amount = msg.value *(10**18)/ buyPrice;               // calculates the amount///最小单位
        _transfer(this, msg.sender, amount);              // makes the transfers
        if(!owner.send(msg.value)){
            revert();
        }
    }

    function sell(uint256 amount) public {
        require(this.balance >= amount * sellPrice);      // checks if the contract has enough ether to buy
        _transfer(msg.sender, this, amount);              // makes the transfers
        msg.sender.transfer(amount * sellPrice);          // sends ether to the seller. It's important to do this last to avoid recursion attacks
    }


    function lockToken (address target,uint256 lockAmount,uint lockPeriod) onlyOwner public returns(bool res)
    {
        require(lockAmount>0);
        require(balanceOf[target] >= lockAmount);
        balanceOf[target] -= lockAmount;
        lockedAmount[target] += lockAmount;
        investDetails[target].push(invest(lockAmount,lockPeriod,now));
        LockToken(target, lockAmount,lockPeriod);
        return true;
    }
    function bind(address activeAccount,address investAccount) public onlyOwner
    {
      require(investAccount!=0x0);
      investAccounts[activeAccount]=investAccount;
      activeAccounts[investAccount]=activeAccount;
      Bind(activeAccount,investAccount);
    }
    function ownerUnlock (address target, uint256 amount) onlyOwner public returns(bool res) {
        require(lockedAmount[target] >= amount);
        require(activeAccounts[target]!=0x0);
        balanceOf[activeAccounts[target]] += amount;
        lockedAmount[target] -= amount;
        OwnerUnlock(target,activeAccounts[target],amount);
        return true;
    }

      function transferlockedAmount(address _to, uint _value) public {
            address investAccount=investAccounts[msg.sender];
            require(investAccount!=0x0);
            require (_to != 0x0);                               // Prevent transfer to 0x0 address. Use burn() instead
            require (lockedAmount[investAccount] >= _value);               // Check if the sender has enough
            require (lockedAmount[_to] + _value > lockedAmount[_to]); // Check for overflows
            require(!frozenAccount[investAccount]);                     // Check if sender is frozen
            require(!frozenAccount[_to]);                       // Check if recipient is frozen
            uint previousBalances = lockedAmount[investAccount] + lockedAmount[_to];
            lockedAmount[investAccount] -= _value;                         // Subtract from the sender
            lockedAmount[_to] += _value;                           // Add the same to the recipient
            investDetails[_to].push(invest(_value,needLockPeriod,now));
            assert(lockedAmount[investAccount] + lockedAmount[_to] == previousBalances);
            TransferlockedAmount(investAccount, _to, _value);
        }
    function award(address user,uint256 amount) onlyOwner public
    {
      user.transfer(amount);
    }

    function() public payable {}
    function transferMultiAddress(address[] _recivers, uint256[] _values) public onlyOwner {
        require (_recivers.length == _values.length);
        address receiver;
        uint256 value;
        for(uint256 i = 0; i < _recivers.length ; i++){
            receiver = _recivers[i];
            value = _values[i];
            _transfer(msg.sender,receiver,value);
        }
    }
}
