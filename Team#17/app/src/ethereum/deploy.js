
// This is a file to deploy the compiled factory contract at .build/projectStore.json
const hdWalletProvider = require("truffle-hdwallet-provider");
const Web3 = require("web3");
const compiledStore = require("../ethereum/build/Store.json");

const provider = new hdWalletProvider(
	"ypu metamask mnemonic",
	"https://rinkeby.infura.io/v3/e8bccfbf91864d7ea8797b0ae8b2d30a"
);

const web3 = new Web3(provider);

const deploy = async () => {
	const accounts = await  web3.eth.getAccounts();
	
	console.log("Attempting to deploy from account ", accounts[0]);

	const result = await new web3.eth.Contract(JSON.parse(compiledStore.interface))
		.deploy({data: "0x" +compiledStore.bytecode})
		.send({gas: "3000000", from: accounts[0]});

	console.log("Whoooopiii!!!, The contract Deployed at ",result.options.address);	
}  
deploy();