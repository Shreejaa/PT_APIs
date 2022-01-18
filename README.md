## Periodic Table KB Project Report
----
*SHREEJAA TALLA*

##### Folder Structure:
```
----- static
           |----- js
	        |----- index.js
----- templates
	   |------ index.html
	   |------ swagger_documentation.html
----- elements.py
----- OpenAPI_PeriodicTable.json
----- OpenAPI_PeriodicTable.yaml
```

### Launch Application:
- To launch application, run python elements.py 
- To launch the frontend application go to http://localhost:5000/
- The front contains documentation hyperlink which is linked to swagger documentation.
- The swagger documentation UI is generated from swagger.io using the OpenAPI_PeriodicTable.json file.
- The frontend takes 5-10 seconds to load the elements as sleep is included to avoid Rdflib synchronization issue.
### Elements API:
- / (frontend UI)
-	/api/docs (swagger documentation)
-	/periodictable/standard_states/
-	/periodictable/standard_state/<string:state>
-	/periodictable/classifications/
-	/periodictable/classification/<string:clss>
-	/periodictable/blocks/
-	/periodictable/block/<string:blk>
-	/periodictable/groups/
-	/periodictable/group/<int:gnum>
-	/periodictable/periods/
-	/periodictable/period/<int:pnum>
-	/periodictable/element/<string:sym>



**Index.js** : Contains ajax calls for the above APIs and results are stored in tables.



**Index.html** :Contains Bootstrap elements and a background image with 5 dropdowns for states, classifications, blocks, periods, and groups. 


