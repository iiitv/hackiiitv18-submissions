
// This file contains functions which interact with the specified project instances. 
const compiledproject = require("../ethereum/build/Project.json");

const {readProjects, web3, deployProject} = require("./store.js");

const getAllProjects = async() => {

	return await readProjects()
		.then( async (deployedProjects) => {
			
		const accounts = await  web3.eth.getAccounts();
		
		const projectDetailList = [];
		for(var i in deployedProjects){		
			const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
			deployedProjects[i]);

			const projectName = await project.methods.projectName().call();
			const projectDesc = await project.methods.projectDesc().call();
			const creatorName = await project.methods.creatorName().call();
			const creatorContact = await project.methods.creatorContact().call();
			
			projectDetailList.push({
				address: deployedProjects[i],
				projectName,
				projectDesc,
				creatorName,
				creatorContact
			});
			// delete project, projectName, projectDesc, creatorContact, creatorName;
		}
		console.log(projectDetailList);
		return projectDetailList;
	});
}

const getProjectDetails = async(address) => {

	const accounts = await  web3.eth.getAccounts();		
	const projectDetailList = {};
	
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
	address);
	
	const projectName = await project.methods.projectName().call();
	const projectDesc = await project.methods.projectDesc().call();
	const creatorName = await project.methods.creatorName().call();
	const creatorContact = await project.methods.creatorContact().call();
	const minContribution = await project.methods.minContribution().call();
	const approversCount = await project.methods.approversCount().call();

	let request  = await project.methods.requests(0).call().catch((err) => {
		console.log("hey1",{projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount})
		return {projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount}
	})

	//console.log(request)
	let i = 0;
	let requestDetail = [];
	
	while(request.description != null){
		requestDetail.push({
			index: i,
			request:
			{
			description: request.description,
			value : request.value
		}});
		i++;
		request = await project.methods.requests(i).call().catch((err) => {
		//console.log("hey2", {projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount})
		return {projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount, requestDetail}
		});
	}
	// delete project,i,request; 	
	console.log("hey3",{projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount, requestDetail})
	return {projectName, projectDesc, creatorName, creatorContact, minContribution, approversCount, requestDetail}
}

// Function to contribute to a project
const contribute = async(address, amount) => {
	
	console.log(address, amount)
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
		address);

	const accounts = await web3.eth.getAccounts();
	console.log(accounts)

	// await project.methods.contribute(web3.utils.toWei(amount, "ether")).send({
		await project.methods.contribute(true).send({
		from: accounts[0],
		value: web3.utils.toWei(amount,"ether")
	});
	console.log("hogya")

}

const createRequest = async(address, description, contact, value, recipient  ) => {
	
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
		address);

	const accounts = await  web3.eth.getAccounts();
	
	await project.methods
			.createRequest(description,contact, value, recipient)
			.send({
				from: accounts[0],
				gas: "3000000"
			});
	console.log("yesss");			
}

const getRequestDetails = async(address, index) => {
	
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
		address);

	const accounts = await  web3.eth.getAccounts();
	let request  = await project.methods.requests(index).call().catch((err) => {
		return null;
	});

	let reqDesc = {description: request.description,
        contact: request.contact,
        value: request.value,
        recipient:  request.recipient,
        complete: request.complete,
        approvalCount: request.approvalCount};
    console.log(reqDesc)
    return reqDesc;  
}

const approveRequest = async(address, index) => {
	
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
		address);

	const accounts = await  web3.eth.getAccounts();
	let request  = await project.methods.approveRequest(index).send({
				from: accounts[0],
				gas: "3000000"
			}).then((xyz) => {
		console.log("Approved!!!!");
		return "Approved";
	}).catch((err) => {
		console.log(err)
		return null;
	});
}

const finalizeRequest = async(address, index) => {
	
	const project = await new web3.eth.Contract((JSON.parse(compiledproject.interface)), 
		address);

	const accounts = await  web3.eth.getAccounts();
	let request  = await project.methods.finalizeRequest(index).send({
				from: accounts[0],
				gas: "3000000"
			}).then((xyz) => {
		console.log("Dne!!!!");
		return "Done";
	}).catch((err) => {
		console.log(err)
		return null;
	});
}
//contribute(1, 124)

//getAllProjects();

//getProjectDetails("0x08a701EC7c1616cE5CBdacb0A65d26783ef8Cb72")

// contribute("0x5E8566CFac62FAC63D85053366282333dB1140d7", "1")

//createRequest("0x08a701EC7c1616cE5CBdacb0A65d26783ef8Cb72", "buying food", "www.food.com", "2", "0x88a4dd75299C3628dc75ba58f238bD3Fff29Ede0")

// getRequestDetails("0x5E8566CFac62FAC63D85053366282333dB1140d7", 0);

//approveRequest("0x08a701EC7c1616cE5CBdacb0A65d26783ef8Cb72", 1);

//finalizeRequest("0x08a701EC7c1616cE5CBdacb0A65d26783ef8Cb72", 1);
 
export {
	getAllProjects,
	getProjectDetails,
	contribute,
	createRequest,
	getRequestDetails,
	approveRequest,
	finalizeRequest
}