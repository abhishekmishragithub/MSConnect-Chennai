# Azure Function in Python   
MS Connect(); Chennai - Empowering every developer to achieve more !!  
Date : 02/02/2019

 
Following 2 methods demonstrates the steps to create Azure Function in Python Runtime usinng VS Code and Core tool.
You can follow either 1st option or 2nd, depending on your choice.


## 1. Creating Azure Function wih VS Code
### Install dependencies

Before you can get started, you should install [Visual Studio Code](https://code.visualstudio.com/). You should also install [Node.JS](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) which includes npm, which is how you will obtain the **Azure Functions Core Tools**. If you prefer not to install Node, see the other installation options in [Core Tools reference](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools).

Run the following command to install the Core Tools package:

    npm install -g azure-functions-core-tools

The Core Tools make use of [.NET Core 2.1](https://dotnet.microsoft.com/download), so you should install that, too. (*Note: Skip if you already have .NET Core 2.1 with Visual Studio*)

Next, install the [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions). Once the extension is installed, click on the Azure logo in the Activity Bar. Under **Azure: Functions**, click **Sign in to Azure...** and follow the on-screen instructions.




### Create an Azure Functions project

Click the **Create New Project…** icon in the **Azure: Functions** panel.

You will be prompted to choose a directory for your app. Choose an empty directory.

You will then be prompted to select a language for your project. Choose python.




### Create a function

Click the **Create Function…** icon in the **Azure: Functions** panel.

You will be prompted to choose a template for your function. We recommend HTTP trigger for getting started.




### Run your function project locally

Press **F5** to run your function app.

The runtime will output a URL for any HTTP functions, which can be copied and run in your browser's address bar.

To stop debugging, press **Shift + F5**.




### Deploy your code to Azure

Click the **Deploy to Function App…** (blue up arrow) icon in the Azure: Functions panel.

When prompted to select a function app, choose *your function app*.  






## 2. Creating Azure Function with Core tool
### Install dependencies

- Follow same process as mentioned above.




### Create an Azure Functions project

In the terminal window or from a command prompt, navigate to an empty folder for your project, and run the following command:

    func init

You will also be prompted to choose a runtime for the project. Select python.(*by pressing down arrow keys*)




### Create a function

To create a function, run the following command:

    func new

This will prompt you to choose a template for your function. We recommend HTTP trigger for getting started.




### Run your function project locally

Run the following command to start your function app:

    func  start

The runtime will output a URL for any HTTP functions, which can be copied and run in your browser's address bar.

To stop debugging, use **Ctrl-C** in the terminal.



### Deploy your code to Azure

To publish your Functions project into Azure, enter the following command:

    func azure functionapp publish msconnectfunction

You may be prompted to sign into Azure. Follow the onscreen instructions.



##### You achieved a milestone !!  :bowtie:
