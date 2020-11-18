# SKR WebAPI Source files

Source : https://ii.nlm.nih.gov/Web_API/SKR_Web_API_V2_3.jar

[Documentation](https://pritishaw.github.io/Analyze-MESH)

To Build Source and Examples  
`bash build.sh <path to source>`  
Built JAR files are available in [`lib`](./lib) folder.  

To Compile a file  
`bash compile.sh <path to .java file>`

To Run a built class   
`bash run.sh <CLASS> <arguments>` 


### Methods in Class [`GenericBatchNew`](./examples/GenericBatchNew.java)
- [`String processor(args[], apikey)`](./examples/GenericBatchNew.java#L91)
Authenticate MTI using API Key
- **[DEPRECATED]** [`String processor(args[], username, password)`](./examples/GenericBatchNew.java#L96)  
Authenticate MTI using username/password

