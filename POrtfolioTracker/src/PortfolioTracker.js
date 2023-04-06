import React, { useState } from 'react';
import axios from 'axios';

const PortfolioTracker = () => {
  const [ethAddress, setEthAddress] = useState('');
  const [ethBalance, setEthBalance] = useState(0);
  const [ethPrice, setEthPrice] = useState(0);
  const [portfolioValue, setPortfolioValue] = useState(0);

  const loadBlockchainData = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/load-data?address=${ethAddress}`);
      const data = response.data;
      setEthBalance(data.eth_balance);
      setEthPrice(data.eth_price_usd);
      setPortfolioValue(data.portfolio_value);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Ethereum Portfolio Tracker</h1>
      <input
        type="text"
        placeholder="Enter your Ethereum address"
        value={ethAddress}
        onChange={(event) => setEthAddress(event.target.value)}
      />
      <button onClick={loadBlockchainData}>Load Data</button>
      <h2>Ethereum Balance: {ethBalance} ETH</h2>
      <h2>Ethereum Price: ${ethPrice}</h2>
      <h2>Portfolio Value: ${portfolioValue}</h2>
    </div>
  );
};

export default PortfolioTracker;
